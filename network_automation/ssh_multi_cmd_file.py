# Cisco device management python script over SSH using Netmiko module
# python -m pip install --upgrade pip
# pip install netmiko

from netmiko import ConnectHandler

'''
username and password can be prompted or stored in an encrypted file
'''

IOSV_L2_S1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.71',
    'username': 'jacky',
    'password': 'cisco'
}

IOSV_L2_S2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.72',
    'username': 'jacky',
    'password': 'cisco'
}

IOSV_L2_S3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.73',
    'username': 'jacky',
    'password': 'cisco'
}

# open a file (iosv2_l2_cisco_design) that contains a series of cisco commands
# the commands list can be updated in the file only without changing this main script
with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = ConnectHandler(IOSV_L2_S1, IOSV_L2_S2, IOSV_L2_S3)

# for loops to iterate through all devices
for device in all_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(lines)
    print(output)