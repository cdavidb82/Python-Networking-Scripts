import wmi


def show_process():
    c = wmi.WMI()
    for process in c.Win32_Process(name='notepad.exe'):
        print(process.ProcessId, process.Name)


if __name__ == '__main__':
    show_process()
