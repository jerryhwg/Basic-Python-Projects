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
    print ("Get running config from Switch " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST) # init a telnet session to a switch ip
    tn.read_until(b"Username: ") # expect "Username: " prompt
    tn.write(user.encode('ascii') + b"\n") # feed the typed username, \n = enter
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n") # feed the typed password and \n (enter)
    tn.write(b"terminal length 0\n") # show the complete configuration without breaks/pauses
    tn.write(b"show run\n") # show running config
    tn.write(b"exit\n")

    readoutput = tn.read_all() # read all data until EOF (take the output)
    saveoutput = open("switch" + HOST, "w") # open up a file with write mode
    saveoutput.write(readoutput.decode('ascii')) # write the output of telnet session in ascii format
    saveoutput.write("\n") # press a carriage return
    saveoutput.close # close the file (important)
    # print(tn.read_all().decode('ascii')) # print the output to the screen (no need)