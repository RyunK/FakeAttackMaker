from scapy.all import IP, UDP, send

spoofed_ip = "192.168.11.129"
target_ip = "192.168.110.128"

# dport=53은 예시로 넣은 포트 번호 (DNS 포트).
# 실제로는 팀 탐지 엔진이 감지하려는 목적지 포트 번호로 바꿔서 사용하면 된다.
udp_packet = IP(src=spoofed_ip, dst=target_ip) / UDP(dport=53)

send(udp_packet, loop=1, verbose=0)