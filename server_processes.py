import wmi
import getpass

def get_server_credentials():
    server = input("Enter server name: ")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    return server, username, password

def processes(server, username, password):
    try:
        connection = wmi.connect_server(server=server, user=username, password=password)
        c = wmi.WMI()
        watch_process = c.watch_for("operation")
        while True:
            new = watch_process()
            print(new.Caption)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    server, username, password = get_server_credentials()
    processes(server, username, password)
