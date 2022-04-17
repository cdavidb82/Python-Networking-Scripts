# arp tool in Scapy Python Library

from scapy.all import *


def arp_monitor_callback(pkt, ARP=None):
    if ARP in pkt and pkt[ARP].op in (1, 2):  # who-has or is-at
        return
    pkt.sprintf("%ARP.hwrc% %ARP.psrc% %ARP.hwdst% %ARP.pdst%")
    sniff(prn=arp_monitor_callback, filter="arp", store=0)


if __name__ == '__main__':
    arp_monitor_callback()
