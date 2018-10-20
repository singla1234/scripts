from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException,AuthenticationException
from paramiko.ssh_exception import SSHException
list_version=["3700 Software","vios_l2 Software"]
with open('devices_details') as f:
    devices_list=f.read().splitlines()
    print(devices_list)

with open('cisco_commands_switch') as f:
    switch_commands=f.read().splitlines()
    print(switch_commands)

with open('cisco_commands_router') as f:
    router_commands=f.read().splitlines()
    print(router_commands)

for device in devices_list:
    print("connecting to "+device)
    ip_address_of_device=device
    ios_device={
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': "lovely",
        'password': "singla",
        'secret': 'cisco'
    }
    try:
        net_connect = ConnectHandler(**ios_device)
    except(AuthenticationException):
        print("Authentication Failure "+ip_address_of_device)
        continue
    except(NetMikoTimeoutException):
        print("Timeout to device "+ip_address_of_device)
        continue
    except(EOFError):
        print("end of file while attempting device "+ip_address_of_device)
        continue
    except(SSHException):
        print("ssh not enabled "+ip_address_of_device)
        continue
    except Exception as unknown_error:
        print("some other error "+unknown_error)
        continue

    #types of devices

    for software_version in list_version:
        print("checking for "+software_version)
        output = net_connect.send_command('show version')
        version = output.find(software_version)
        if version>0:
            print("software version found "+software_version)
            break
        else:
            print("version not found")

    if software_version=="3700 Software":
        print("running commands for router "+ip_address_of_device)
        output = net_connect.send_command("show ip int brief")
    elif software_version=="vios_l2 Software":
        print("running commands for switch " + ip_address_of_device)
        output = net_connect.send_command("show vlan brief")
    print(output)


