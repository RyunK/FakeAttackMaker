import argparse
# 실행 시 --scan 옵션으로 스캔 종류를 선택할 수 있도록 argparse를 가져온다.

from config import TARGET_IP, DEFAULT_COUNT, DEFAULT_INTERVAL
# config.py 파일에 저장되어 있는 설정값을 가져온다.
# TARGET_IP : 스캔(테스트) 대상 IP 주소
# DEFAULT_COUNT : 몇 개의 포트를 스캔할 것인지 (예: 30이면 1~30번 포트)
# DEFAULT_INTERVAL : 패킷 하나를 보낸 후 대기할 시간(초)

from scapy.all import IP, TCP, send
# Scapy에서 IP 패킷 생성, TCP 패킷 생성, 패킷 전송 기능을 가져온다.

import time
# time.sleep() 함수를 사용하기 위해 time 모듈을 가져온다.

from tqdm import tqdm
# 반복문의 진행률(Progress Bar)을 화면에 표시하기 위해 tqdm을 가져온다.

NAME = "SYN / FIN / Xmas Scan"
# 현재 공격(테스트) 모듈의 이름을 저장한다.

SCAN_FLAGS = {
    "syn": "S",
    "fin": "F",
    "xmas": "FPU",
}
# 스캔 종류별로 사용할 TCP 플래그 조합.
# syn  : SYN 플래그만 켠 패킷
# fin  : FIN 플래그만 켠 패킷
# xmas : FIN + PSH + URG를 동시에 켠 패킷 (크리스마스 트리 전구처럼 여러 플래그가 켜져 있다고 해서 붙은 이름)


def scan(scan_name: str, flags: str):
    # 지정한 플래그로 포트 1~DEFAULT_COUNT까지 스캔 패킷을 전송한다.

    for port in tqdm(range(1, DEFAULT_COUNT + 1), desc=f"{scan_name} scan"):
        # 1번 포트부터 DEFAULT_COUNT번 포트까지 하나씩 반복한다.
        # tqdm은 현재 진행률을 화면에 보여준다.

        packet = (
            IP(dst=TARGET_IP) /
            TCP(dport=port, flags=flags)
        )
        # 하나의 TCP 패킷을 생성한다.
        # 목적지 IP는 TARGET_IP
        # 목적지 포트는 현재 반복 중인 port
        # flags는 인자로 받은 플래그 조합

        send(packet, verbose=False)
        # 생성한 패킷을 실제 네트워크로 전송한다.
        # verbose=False는 Scapy의 불필요한 출력 메시지를 숨긴다.

        time.sleep(DEFAULT_INTERVAL)
        # 패킷을 하나 보낸 후 DEFAULT_INTERVAL초 동안 기다린다.


def run(scan_types: list[str]):
    # 지정된 스캔 종류들을 순서대로 실행한다.

    for i, scan_type in enumerate(scan_types):
        # scan_types 리스트에 담긴 스캔 종류를 하나씩 꺼내 반복한다.

        scan(scan_type.upper(), SCAN_FLAGS[scan_type])
        # 해당 스캔 종류의 플래그로 scan()을 실행한다.

        if i < len(scan_types) - 1:
            # 마지막 스캔이 아니라면

            time.sleep(1)
            # 다음 스캔을 시작하기 전 1초 동안 기다린다.
            # 탐지 로그가 겹치는 것을 조금 줄일 수 있다.


if __name__ == "__main__":
    # 현재 이 파일을 직접 실행했을 때만 아래 코드를 실행한다.

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scan",
        choices=list(SCAN_FLAGS.keys()) + ["all"],
        default="all",
        help="실행할 스캔 종류 (syn / fin / xmas / all)",
    )
    args = parser.parse_args()
    # 실행 시 --scan 옵션 값을 읽어온다. 지정하지 않으면 "all"이 기본값이다.

    scan_types = list(SCAN_FLAGS.keys()) if args.scan == "all" else [args.scan]
    # "all"이면 syn, fin, xmas 전부 실행하고
    # 특정 종류를 지정했으면 그 하나만 실행한다.

    run(scan_types)
    # 선택된 스캔 종류를 순서대로 실행한다.