# Set the password in the password file, use MD5 encryption

import hashlib

# function to prompt for a password and compare it against the hashed
# password passed in
def passwordAttempt(pTheHashedPassword):

    wPassword = input('What''s the password : ')

    if hashlib.md5(wPassword.encode()).hexdigest() == pTheHashedPassword:
        return (True)
    else:
        return (False)


# Get the hashed password from the password file
wPasswordFile = open('password.txt','r')
wHashedPassword = wPasswordFile.read()
wPasswordFile.close()


# How many attempts are we going to allow?
wMaxAttempts = 3
wAttempts = 0

wAttempts += 1
wSuccess = passwordAttempt(wHashedPassword)
while ((wAttempts < wMaxAttempts) and (wSuccess == False)):
    wAttempts += 1
    wSuccess = passwordAttempt(wHashedPassword)

# At this point we've either run out of goes or got the password correct
if wSuccess==True:
    print('Welcome to system X')
else:
    print('Login Failed - Authorities Informed, please wait for Police!')



