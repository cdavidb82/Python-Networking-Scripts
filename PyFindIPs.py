# IP Scanner

import ifaddr
import pprint

def get_network_adapters():
    return ifaddr.get_adapters()

def print_adapter_ips(adapters):
    pp = pprint.PrettyPrinter(indent=1)
    for adapter in adapters:
        pp.pprint(f'IPs of network adapter {adapter.nice_name}')
        for ip in adapter.ips:
            print(f'  {ip.ip}/{ip.network_prefix}')

def main():
    adapters = get_network_adapters()
    print_adapter_ips(adapters)

if __name__ == '__main__':
    main()
