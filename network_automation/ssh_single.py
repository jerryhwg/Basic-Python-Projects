# Cisco device management python script over SSH using Netmiko module
# python -m pip install --upgrade pip
# pip install netmiko

from netmiko import ConnectHandler

'''
username and password can be prompted or stored in an encrypted file
'''

IOSV_L2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.71',
    'username': 'jacky',
    'password': 'cisco'
}

net_connect = ConnectHandler(**IOSV_L2)

output = net_connect.send_command('show ip int brief')
print(output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)

for n in range(2,21):
    print("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name PYTHON_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)