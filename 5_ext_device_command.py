from netmiko import ConnectHandler

with open('cisco_commands') as f:
    lines=f.read().splitlines()
    print(lines)

with open('devices_details') as f:
    devices_list=f.read().splitlines()
    print(devices_list)

for device in devices_list:
    print("connecting to"+device)
    ip_address_of_device=device
    print(ip_address_of_device)
    ios_device={
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': 'lovely',
        'password': 'singla',
        'secret': 'cisco'
    }

    net_connect = ConnectHandler(**ios_device)
    output=net_connect.enable()
    print(output)
    output = net_connect.send_config_set(lines)
    print(output)
