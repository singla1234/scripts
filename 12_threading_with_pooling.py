from simplecrypt import encrypt, decrypt
from pprint import pprint
from netmiko import ConnectHandler
import json
from time import time
from multiprocessing
# ------------------------------------------------------------------------------
def read_devices(devices_filename):
    devices = {}  # create our dictionary for storing devices and their info
    with open(devices_filename) as devices_file:
        for device_line in devices_file:
            device_info = device_line.strip().split(',')  # extract device info from line
            device = {'ipaddr': device_info[0],'type': device_info[1],'name': device_info[2]}  # create dictionary of device objects ...
            devices[device['ipaddr']] = device  # store our device in the devices dictionary
            # note the key for devices dictionary entries is ipaddr
    print("--- devices info ---")
    pprint(devices)
    return devices
# ------------------------------------------------------------------------------
def read_device_creds(device_creds_filename, key):
    print("---getting credentials---")
    with open(device_creds_filename, 'rb') as device_creds_file:
        device_creds_json = decrypt(key, device_creds_file.read())
        device_creds_list = json.loads(device_creds_json)
    pprint(device_creds_list)
    print("--- device_creds ---")
    # convert to dictionary of lists using dictionary comprehension
    device_creds = {dev[0]: dev for dev in device_creds_list}
    pprint(device_creds)
    return device_creds
# ------------------------------------------------------------------------------
def config_worker(device, creds):
    # ---- Connect to the device ----
    if device['type'] == 'cisco_ios':
        device_name='cisco_ios'
    elif device['type'] == 'router':
        device_name= 'router'
    print('Connecting to device {0}'.format(device['ipaddr']))

    # ---- Connect to the device
    session = ConnectHandler(device_type=device_name,ip=device['ipaddr'],username=creds[1], password=creds[2])

    # session = ConnectHandler( device_type=device_type, ip='172.16.0.1',  # Faking out IP address for now
    #                                                   username=creds[1], password=creds[2] )
    if device_name == 'cisco_ios':
        # ---- Use CLI command to get configuration data from device
        print('---- Getting configuration from device')
        config_data = session.send_command('show vlan brief')
        print(config_data)

    if device_name == 'router':
        # ---- Use CLI command to get configuration data from device
        print('---- Getting configuration from device')
        config_data = session.send_command('show ip interface brief')

    # ---- Write out configuration information to file
    config_filename = 'config-' + device['ipaddr']  # Important - create unique configuration file name

    print('---- Writing configuration: ', config_filename)
    with open(config_filename, 'w') as config_out:
        config_out.write(config_data)
    session.disconnect()
    return


# ==============================================================================
# ---- Main: Get Configuration
# ==============================================================================

devices = read_devices('devices_filename')
creds = read_device_creds('encrypted-device-creds', 'lovely')

num_threads = int(raw_input( '\nNumber of threads (3): ' ) or '3')
#num_threads= int( num_threads_str )
#---- Create list for passing to config worker
config_params_list = []
#for ipaddr,device in devices.items():
#   config_params_list.append((device, creds[ipaddr]))
#print(config_params_list)
starting_time = time()
print("--- Creating threadpool, launching get config threads")
threads = ThreadPool(num_threads)
print("Creating threadpool, launching get config threads")
threads = ThreadPool(num_threads)
for ipaddr,device in devices.items():
    results = threads.map(target=config_worker,args=(device, creds[ipaddr]))

threads.close()
threads.join()
print("---- End get config threading ----")
elapsed_time=time() - starting_time
print(elapsed_time)
