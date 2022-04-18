import socket,os
if os.name == "nt":  # for Windows
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind("10.10.2.107", 0)  # your ip
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
else:
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x800))  # for *Nix

while True:
    pkt = s.recvfrom(65565)  # print output on terminal