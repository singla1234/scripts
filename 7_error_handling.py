from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import NetMikoTimeoutException,AuthenticationException
from paramiko.ssh_exception import SSHException

user_name=raw_input("enter your ssh username:")
password=getpass()
with open('cisco_commands') as f:
    lines=f.read().splitlines()
    print(lines)

with open('devices_details') as f:
    devices_list=f.read().splitlines()
    print(devices_list)

for device in devices_list:
    print("connecting to"+device)
    ip_address_of_device=device
    ios_device={
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': user_name,
        'password': password,
        'secret': 'cisco'
    }
    try:
        net_connect = ConnectHandler(**ios_device)
    except(AuthenticationException):
        print("Authentication Failure"+ip_address_of_device)
        continue
    except(NetMikoTimeoutException):
        print("Timeout to device"+ip_address_of_device)
        continue
    except(EOFError):
        print("end of file while attempting device"+ip_address_of_device)
        continue
    except(SSHException):
        print("ssh not enabled"+ip_address_of_device)
        continue
    except Exception as unknown_error:
        print("some other error"+unknown_error)
        continue

    output=net_connect.enable()
    print(output)
    output = net_connect.send_config_set(lines)
    print(output)
