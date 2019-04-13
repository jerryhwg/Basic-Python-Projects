from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

username = input("Enter your SSH username: ")
password = getpass()

# commands_file_swtich file locally
with open('commands_file_switch') as f:
    command_list_switch = f.read().splitlines()

# commands_file_router file locally
with open('commands_file_router') as f:
    command_list_router = f.read().splitlines()

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

    # Types of devices
    list_versions = ['vios_l2-ADVENTERPRISEK9-M', 'VIOS-ADVENTERPRISEK9-M']

    # Check software versions of the current iterated device
    for software_ver in list_versions:
        print("Checking for " + software_ver)
        output_version = net_connect.send_command('show version')
        int_version = 0 # Reset integer value
        int_version = output_version.find(software_ver) # Check software version
        if int_version > 0:
            print("Software version found: " + software_ver)
            break
        else:
            print("Not found " + software_ver)

    # Moving on to the next stage
    if software_ver == 'vios_l2-ADVENTERPRISEK9-M':
        print("Running " + software_ver + " commands")
        output = net_connect.send_config_set(command_list_switch)
    elif software_ver == 'VIOS-ADVENTERPRISEK9-M':
        print("Running " + software_ver + " commands")
        output = net_connect.send_config_set(command_list_router)
    print(output)


# devices_file example
'''
192.168.100.71
192.168.100.72
192.168.100.73
192.168.100.74
192.168.100.75
'''

# commands_list_switch example
'''
ip name-server 8.8.8.8
ip domain-lookup
username test password test
router ospf 1
network 0.0.0.0 255.255.255.255 area 0
'''