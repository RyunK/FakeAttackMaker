from config import TARGET_IP, DEFAULT_INTERVAL
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send
from tqdm import tqdm
import time

NAME = "NULL Scan"

start_port = 1
end_port = 100

def run():
    # Count만큼 패킷을 보내고, Interval만큼 대기
    for port in tqdm(range(start_port, end_port +1)):
        pkt = IP(dst=TARGET_IP) / TCP(dport=port, flags=0)

        send(pkt, verbose=False)
        time.sleep(DEFAULT_INTERVAL)

if __name__ == "__main__":
    run()
