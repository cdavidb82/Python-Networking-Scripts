import ifaddr
import pprint

adapters = ifaddr.get_adapters()
pp = pprint.PrettyPrinter(indent=1)


def find_ip():
    for adapter in adapters:
        pp.pprint(f'IPs of network adapter {adapter.nice_name}')
        for ip in adapter.ips:
            print(' %s%s' % (ip.ip, ip.network_prefix))


if __name__ == '__main__':
    find_ip()
