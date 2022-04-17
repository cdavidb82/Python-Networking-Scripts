
import wmi
import getpass


def processes():
    connection = wmi.connect_server(server='server-name', user='username', password=getpass.getpass())
    c = wmi.WMI()
    watch_process = c.watch_for("operation")
    while True:
        new = watch_process()
        print(new.Caption)


if __name__ == '__main__':
    processes()
