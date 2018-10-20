from netmiko import ConnectHandler

iosv_l2={
    'device_type':'cisco_ios',
    'ip':'192.168.122.72',
    'username':'lovely',
    'password':'singla',
    'secret':'cisco'
}
net_connect = ConnectHandler(**iosv_l2)
output=net_connect.enable()
print(output)

output = net_connect.send_command('show ip int brief')
print(output)

config_commands = [ 'int loop 0','ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)

for n in range(22,24):
    print("creating vlan"+str(n))
    config_commands = ["vlan "+str(n),"name python vlan "+str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)
