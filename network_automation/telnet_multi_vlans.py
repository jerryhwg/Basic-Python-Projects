import getpass
import telnetlib

user = input("Enter your telnet username")
password = getpass.getpass()

# save ip addresses (line by line) in a text file 'myswitches'
f = open ('myswitches') 

# one loop for each individual switch
# second loop for each vlan

for IP in f:
    IP=IP.strip() # remove any trail space
    print ("Configuring Switch " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST) # init a telnet session to a switch ip
    tn.read_until(b"Username: ") # expect "Username: " prompt
    tn.write(user.encode('ascii') + b"\n") # feed the typed username, \n = enter
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n") # feed the typed password and \n (enter)
    tn.write(b"conf t\n") # enter config mode (no enable necessary for the user has priviledge 15)

    for n in range(2,21): # for vlan 2 ~ 20
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n") # str(n) to concatenate int and string
        tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")
    
    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii')) # read all data until EOF (print the output to the screen)