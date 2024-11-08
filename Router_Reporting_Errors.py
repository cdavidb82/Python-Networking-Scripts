#!usr/bin/env python3

import csv
import getpass
from argparse import ArgumentParser

import netmiko
import paramiko


def connect_to_device(device_ip, ssh_username, ssh_password):
    try:
        ssh_session = netmiko.ConnectHandler(
            device_type='cisco_ios',
            ip=device_ip,
            username=ssh_username,
            password=ssh_password
        )
        return ssh_session
    except (netmiko.ssh_exception.NetMikoTimeoutException, paramiko.ssh_exception.SSHException) as s_error:
        print(f"Failed to connect to {device_ip}: {s_error}")
        return None


def execute_command(ssh_session, command):
    try:
        output = ssh_session.send_command(command)
        return output
    except (netmiko.ssh_exception.NetMikoTimeoutException, paramiko.ssh_exception.SSHException) as s_error:
        print(f"Failed to execute command on {ssh_session.ip}: {s_error}")
        return None


def main():
    parser = ArgumentParser(description='Arguments for running oneLiner.py')
    parser.add_argument('-c', '--csv', required=True, action='store', help='Location of CSV file')

    args = parser.parse_args()
    ssh_username = input("SSH Username: ")
    ssh_password = getpass.getpass('SSH Password: ')
    with open(args.csv, "r") as file:
        reader = csv.DictReader(file)
        for device_row in reader:
            ssh_session = connect_to_device(device_row['device_ip'], ssh_username, ssh_password)
            if ssh_session:
                print(f"+++++     {device_row['device_ip']}     +++++")
                output = execute_command(ssh_session, 'terminal length 30')
                if output:
                    print(output)
                ssh_session.disconnect()


if __name__ == '__main__':
    main()