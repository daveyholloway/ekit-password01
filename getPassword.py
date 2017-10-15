# Set the password in the password file, use MD5 encryption

import hashlib

wPassword = input('Enter the required password : ')


wPasswordFile = open('password.txt','w')
wPasswordFile.write(hashlib.md5(wPassword.encode()).hexdigest())
wPasswordFile.close()


