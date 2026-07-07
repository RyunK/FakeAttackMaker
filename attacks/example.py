from config import TARGET_IP, DEFAULT_TARGET_PORT, DEFAULT_COUNT, DEFAULT_INTERVAL
from scapy.all import IP, UDP, Raw, send
import time
from tqdm import tqdm


NAME = "EXAMPLE Attack"

def run():
    # print("EXAMPLE Attack 실행")
    payload = b"A" * 1400   # 큰 응답을 흉내

    # Count만큼 패킷을 보내고, Interval만큼 대기
    for _ in tqdm(range(DEFAULT_COUNT)):
        packet = (
            IP(src="8.8.8.8", dst=TARGET_IP) /
            UDP(sport=53, dport=DEFAULT_TARGET_PORT) /
            Raw(payload)
        )

        # 실제로 패킷을 보내면 안돼서 주석 처리
        # send(packet, verbose=False)
        time.sleep(DEFAULT_INTERVAL)

if __name__ == "__main__":
    run()
