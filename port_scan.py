#!/bin/python3 

import socket 
import sys 
import os
from datetime import datetime as dt
import pyfiglet
import subprocess

#add threading 
#add ip regex 

max_number_of_ports = 65535

subprocess.call('clear', shell=True) 

#Check the date and time the scan was started
t1 = dt.now()

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

if len(sys.argv) != 3 or int(sys.argv[2]) > max_number_of_ports:
	print("Invalid Arguments!")
	print(">>{} <target> <number of ports>".format(sys.argv[0]))
	exit()
else:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4 
	portsToScan = int(sys.argv[2])
	

def addHashtags():
	print("*" * 30 )




addHashtags()
print("Scanning target " + target)
addHashtags()

with open("port_scan.txt", "w") as f:
	f.write(pyfiglet.figlet_format("PORT SCANNER"))
	f.write("Scanning target {}\n".format(target))
	
	try:
		for port in range(1, portsToScan):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target, port))
			if result == 0: 
				print("Port {} is open". format(port))
				f.write("Port {} is open\n". format(port))
			

			s.close()

	except KeyboardInterrupt:
		print("\n Exiting program.")
		sys.exit()

	except socket.gaierror: 
		print("Hostname could not be resolved.")
		sys.exit()

	except socket.error:
		print("Could not connect to server.")
		sys.error()
	t2 = dt.now()
	totalTime = t2 - t1
	
	f.write("Scan completed in {}".format(totalTime))

addHashtags()
 
print("Scan completed in {}".format(totalTime))