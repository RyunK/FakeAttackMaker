from config import (TARGET_IP, SRC_IP_LIST, DEFAULT_COUNT, DEFAULT_INTERVAL)
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import send
from tqdm import tqdm
import time

NAME = "UDP Scan"

def run():

    for port in tqdm(range(1, DEFAULT_COUNT + 1), desc="UDP Scan"):

        packet = (
            IP(
                src=SRC_IP_LIST[0],
                dst=TARGET_IP
            )
            /
            UDP(
                dport=port
            )
        )

        send(packet, verbose=False)

        time.sleep(DEFAULT_INTERVAL)


if __name__ == "__main__":
    run()