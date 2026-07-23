from scapy.all import IP, UDP, Raw, send
import random

TEST_DNS_SERVERS  = [
    "10.10.0.10",
    "10.10.0.11",
    "10.10.0.12",
    "10.10.0.13",
    "10.10.0.14",
]

def send_amp_random_packet(target_ip, target_port, sport, payload):

    packet = (
            IP(src=random.choice(TEST_DNS_SERVERS), dst=target_ip) /
            UDP(sport=sport, dport=target_port) /
            Raw(payload)
        )

    # 실제로 패킷을 보내면 안돼서 주석 처리
    send(packet, verbose=False)