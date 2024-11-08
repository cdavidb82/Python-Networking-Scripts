import ipaddress
import subprocess
import platform


def ping_network(ip_net):
    all_hosts = list(ip_net.hosts())  # Get all hosts on that network

    info = subprocess.STARTUPINFO()  # Hides console window
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE

    for host in all_hosts:
        ping_cmd = ['ping', '-n', '1', '-w', '500', str(host)] if platform.system().lower() == 'windows' else ['ping', '-c', '1', '-w', '1', str(host)]
        output = subprocess.Popen(
            ping_cmd,
            stdout=subprocess.PIPE,
            startupinfo=info,
        ).communicate()[0]

        if "Destination host unreachable" in output.decode('utf-8'):
            print(str(host), 'is Offline')
        elif "Request timed out" in output.decode('utf-8'):
            print(str(host), 'is unreachable')
        else:
            print(str(host), 'is reachable')


if __name__ == '__main__':
    print("Program will start pinging network....")
    try:
        ip_net = ipaddress.ip_network(u'10.1.10.0/24')  # Create the network
        ping_network(ip_net)
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        exit(1)
    except Exception as e:
        print("An error occurred: ", str(e))
