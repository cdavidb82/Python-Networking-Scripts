# IP Scanner
import ifaddr # type: ignore
import pprint

def get_network_adapters():
    """Retrieve a list of network adapters."""
    return ifaddr.get_adapters()

def print_adapter_ips(adapters):
    """Print the IP addresses of the given network adapters."""
    pp = pprint.PrettyPrinter(indent=1)
    for adapter in adapters:
        pp.pprint(f'IPs of network adapter {adapter.nice_name}')
        for ip in adapter.ips:
            print(f'  {ip.ip}/{ip.network_prefix}')

def main():
    """Main entry point of the program."""
    adapters = get_network_adapters()
    if adapters:
        print_adapter_ips(adapters)
    else:
        print("No network adapters found.")

if __name__ == '__main__':
    main()
