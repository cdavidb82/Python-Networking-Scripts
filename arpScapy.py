from scapy.all import ARP, sniff

def arp_monitor_callback(pkt):
    if pkt.haslayer(ARP):
        if pkt[ARP].op in (1, 2):  # who-has or is-at
            print(f"Source IP: {pkt[ARP].psrc}, Source MAC: {pkt[ARP].hwsrc}, Destination IP: {pkt[ARP].pdst}, Destination MAC: {pkt[ARP].hwdst}")
        else:
            print(f"ARP packet received: {pkt.summary()}")
    else:
        print(f"Non-ARP packet received: {pkt.summary()}")

if __name__ == '__main__':
    sniff(prn=arp_monitor_callback, filter="arp", store=0)