from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

username = input("Enter your SSH username: ")
password = getpass()

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
        'username': username,
        'password': password
    }

    # Exception handling allows the remaining codes to still continue in any exception occurrences
    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException): # authentication failure case handling
        print("Authentication failure: " + ip_address_of_device)
        continue
    except (NetMikoTimeoutException): # devices are offline or unreachable
        print("Timeout to device: " + ip_address_of_device)
        continue
    except (EOFError):
        print("End of file while attempting device" + ip_address_of_device)
        continue
    except (SSHException): # SSH is not enabled
        print("SSH Issue. Are you sure SSH is enabled" + ip_address_of_device)
        continue
    except Exception as unknown_error:
        print("Some other error: " + unknown_error)
        continue

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