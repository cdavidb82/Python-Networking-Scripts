import ipaddress
import subprocess


def ping_network():
    ip_net = ipaddress.ip_network(u'10.1.10.0/24')  # Create the network
    all_hosts = list(ip_net.hosts())  # Get all hosts on that network

    info = subprocess.STARTUPINFO()  # Hides console window
    info.dwFlags != subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE

    for i in range(len(all_hosts)):
        output = subprocess.Popen(
            ['ping', '-n', '1', '-w', '500', str(all_hosts[i])],
            stdout=subprocess.PIPE,
            startupinfo=info,
        ).communicate()[0]

        if "Destination host unreachable" in output.decode('utf-8'):
            print(str(all_hosts[i]), 'is Offline')
        elif "Request timed out" in output.decode('utf-8'):
            print(str(all_hosts[i]), 'is unreachable')
        else:
            print(str(all_hosts[i]), 'is reachable')


if __name__ == '__main__':
    print("Program will start pinging network....")
    try:
        ping_network()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        exit(1)
