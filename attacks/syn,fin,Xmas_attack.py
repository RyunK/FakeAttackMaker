import argparse
from config import TARGET_IP, DEFAULT_COUNT, DEFAULT_INTERVAL
from scapy.all import IP, TCP, send
import time
from tqdm import tqdm

NAME = "SYN / FIN / Xmas Scan"

SCAN_FLAGS = {
    "syn": "S",
    "fin": "F",
    "xmas": "FPU",
}


def scan(scan_name: str, flags: str):
    for port in tqdm(range(1, DEFAULT_COUNT + 1), desc=f"{scan_name} scan"):
        packet = (
            IP(dst=TARGET_IP) /
            TCP(dport=port, flags=flags)
        )
        send(packet, verbose=False)
        time.sleep(DEFAULT_INTERVAL)


def run(scan_types: list[str] = None):
    # main.py의 메뉴 시스템은 run()을 인자 없이 호출하므로,
    # 기본값(None)일 때는 SYN/FIN/Xmas 전부 실행하도록 한다.
    if scan_types is None:
        scan_types = list(SCAN_FLAGS.keys())

    for i, scan_type in enumerate(scan_types):
        scan(scan_type.upper(), SCAN_FLAGS[scan_type])

        if i < len(scan_types) - 1:
            time.sleep(1)


if __name__ == "__main__":
    # 이 파일을 직접 실행할 때만 --scan 옵션으로 특정 스캔만 고를 수 있다.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scan",
        choices=list(SCAN_FLAGS.keys()) + ["all"],
        default="all",
        help="실행할 스캔 종류 (syn / fin / xmas / all)",
    )
    args = parser.parse_args()

    scan_types = list(SCAN_FLAGS.keys()) if args.scan == "all" else [args.scan]
    run(scan_types)