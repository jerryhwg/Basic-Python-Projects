# Network Automation

### How to enable SSH on a Cisco switch

```bash
enable
conf t
username jacky pass cisco
username jacky priv 15

line vty 0 4
 login local
 transport input all

ip domain-name example.com
crypto key generate rsa
1024

end
wr
```

### How to encrypt a password file

Using simple-crypt 4.1.7

```python
pip install simple-crypt

from simplecrypt import encrypt, decrypt
ciphertext = encrypt('password', plaintext)
plaintext = decrypt('password', ciphertext)
```

### Useful Projects

* [Netmiko](https://pynet.twb-tech.com/blog/automation/netmiko.html)
* [Napalm](https://napalm-automation.net/)
* [Nornir](https://github.com/nornir-automation/nornir)