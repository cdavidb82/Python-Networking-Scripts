import wmi

def show_process(process_name):
    try:
        c = wmi.WMI()
        for process in c.Win32_Process(name=process_name):
            print(f"Process ID: {process.ProcessId}, Process Name: {process.Name}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    process_name = 'notepad.exe'
    show_process(process_name)