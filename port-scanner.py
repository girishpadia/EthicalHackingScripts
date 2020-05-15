#!/bin/python3
#Author: Girish Padia
#Refernce: Udemy Course: Practical Ethical Hacking by TheCyberMentor @thecybermentor
import sys
import socket
from datetime import datetime

# Define our traget 
if len(sys.argv) == 4:
    try:
        target = socket.gethostbyname(sys.argv[1]) #converting hostname to ip address
        fromPort = int(sys.argv[2])
        toPort =   int(sys.argv[3]) + 1
    except socket.gaierror:
        print("Hostname couldn't be resolved")
        sys.exit()
    except ValueError:
        print("fromPort or toPort must be integer values")
        sys.exit()
else:
    print("Invalid amount of arguments.")
    print("Syntax: phthon3 port-scanner.ph fromPort toPort")
    sys.exit()

# Add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("TIme started: "+str(datetime.now()))
print("-" * 50)

try:
    for port in range(fromPort,toPort):
        #print("Trying port {} ".format(port))
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #result is zero if port is open
        if result == 0:
            try:
                serviceName = socket.getservbyport(port)
            except socket.error:
                print("Port open "+str(port)+" ServiceName : Undefined")
            print("Port open "+str(port)+" ServiceName : "+serviceName)
        s.close()
except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()
except socket.gaierror:
    print("Hostname couldn't be resolved")
    sys.exit()

except socket.error:
    print("Couldn't connect to server");
    sys.exit()
