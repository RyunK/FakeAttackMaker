from config import TARGET_IP, DEFAULT_TARGET_PORT, DEFAULT_COUNT, DEFAULT_INTERVAL
from scapy.all import IP, UDP, Raw, send
import time

NAME = "EXAMPLE Attack"

def run():
    # print("EXAMPLE Attack 실행")
    payload = b"A" * 1400   # 큰 응답을 흉내

    while True:
        packet = (
            IP(src="8.8.8.8", dst=TARGET_IP) /
            UDP(sport=53, dport=53000) /
            Raw(payload)
        )

        # send(packet, verbose=False)
        time.sleep(0.005)

if __name__ == "__main__":
    run()
