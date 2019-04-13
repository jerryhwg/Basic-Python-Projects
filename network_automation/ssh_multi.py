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

all_devices = ConnectHandler(IOSV_L2_S1, IOSV_L2_S2, IOSV_L2_S3)

# nested loops
for device in all_devices:
    net_connect = ConnectHandler(**device)
    for n in range(2,21):
        print("Creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name PYTHON_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)