from netmiko import ConnectHandler

with open('commands_file') as f:
    command_list = f.read().splitlines()

with open('devices_file') as f:
    devices_list = f.read().splitlines()

for device in devices_list:
    print ("Connecting to device " + device)
    ip_address_of_device = device
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': 'jacky',
        'password': 'cisco'
    }

    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_config_set(command_list)
    print(output)


# devices_file example
'''
192.168.100.71
192.168.100.72
192.168.100.73
192.168.100.74
192.168.100.75
'''

# commands_file example
'''
ip name-server 8.8.8.8
ip domain-lookup
username test password test
router ospf 1
network 0.0.0.0 255.255.255.255 area 0
'''