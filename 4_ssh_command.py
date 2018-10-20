from netmiko import ConnectHandler

device_1={
    'device_type':'cisco_ios',
    'ip':'192.168.122.72',
    'username':'lovely',
    'password':'singla',
    'secret':'cisco'
}

device_2={
    'device_type':'cisco_ios',
    'ip':'192.168.122.82',
    'username':'lovely',
    'password':'singla',
    'secret':'cisco'
}

with open('cisco_commands') as f:
    lines=f.read().splitlines()
    print(lines)

all_devices=[device_1,device_2]

for device in all_devices:
    net_connect = ConnectHandler(**device)
    output=net_connect.enable()
    print(output)

    output = net_connect.send_command('show ip int brief')
    print(output)

    config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)

    for n in range(2,4):
        print("deleting vlan" + str(n))
        config_commands = ["no vlan " + str(n)]
        output = net_connect.send_config_set(config_commands)
        print("vlan deleted"+str(n))
        print(output)
