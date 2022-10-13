from gc import disable
import sys
from pwn import * 

#param checker
if len(sys.argv) != 3: 
	print("Invalid Arguments")
	print(">> {} <sha256sum> <wordlist.txt>".format(sys.argv[0]))
	exit()

wanted_hash = sys.argv[1]
password_file = sys.argv[2]
attempts = 0

with log.progress("Attempting to crack {}!".format(wanted_hash)) as p: 
	with open(password_file,"r", encoding="latin-1") as password_list:
		for password in password_list:
			password = password.strip().encode('latin-1')
			password_hash = sha256sumhex(password)
			p.status("[{}] {} == {}".format(attempts,password.decode('latin-1'), password_hash))
			if password_hash == wanted_hash:
				p.success("Password hash found after {} attempts! {} hashes to {}!".format(attempts,password.decode('latin-1'),password_hash))
				exit()
			attempts+=1
		p.failure("Password hash not found!")
		print
