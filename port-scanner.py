#!/bin/python3
#Author: Girish Padia
#Refernce: Udemy Course: Practical Ethical Hacking by TheCyberMentor @thecybermentor
import sys
import socket
import threading
from datetime import datetime

# Define our traget 
ports = []
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
    print("Syntax: phthon3 port-scanner.py HostName|IPAddress fromPort toPort")
    sys.exit()

# Add a pretty banner
print("Before running this script, make sure that the host is up and running")
print("-" * 50)
print("Scanning target "+target)
print("TIme started: "+str(datetime.now()))
print("-" * 50)


def portScan (fromPort,toPort):
    try:
        for port in range(fromPort,toPort):
            # print("Trying port {} ".format(port))
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port)) #result is zero if port is open
            if result == 0:
                #print("Port open "+str(port)+" ServiceName : "+serviceName)
                ports.append(port)
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
#x1 = threading.Thread(target=portScan, args=(80,443))
#x1.start()

x = threading.Thread(target=portScan, args=(80,180))
x.start()
x1 = threading.Thread(target=portScan, args=(181,281))
x1.start()
""" x2 = threading.Thread(target=portScan, args=(281,381))
x2.start()
x3 = threading.Thread(target=portScan, args=(381,443))
x3.start()
 """

x.join()
x1.join()

ports.sort()

if(len(ports) != 0):
    for x in ports:
        try:
            serviceName = socket.getservbyport(ports[x])
        except socket.error:
            print("Port open "+str(ports[x])+" ServiceName : Undefined")
        print("Port open "+str(ports[x])+" ServiceName : "+serviceName)
else:
    print("There are no open ports observed")
