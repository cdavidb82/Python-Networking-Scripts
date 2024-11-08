import socket, os

def create_raw_socket():
    if os.name == "nt":  # for Windows
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        s.bind("10.10.2.107", 0)  # your ip
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    else:
        s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x800))  # for *Nix
    return s

def main():
    s = create_raw_socket()
    while True:
        try:
            pkt = s.recvfrom(65565)  # print output on terminal
            print(pkt)
        except KeyboardInterrupt:
            print("Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()