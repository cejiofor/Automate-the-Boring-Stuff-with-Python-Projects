##! python3
# strong-password.py - A function that tuses regular expressions to make sure a password is strong. 

## Password Requirements: 
# Has at least eight characters
# Contains both uppercase and lowercase characters 
# Has at least one digit.

import re

def passwordCheck(password):
    passwordStrong = True

    characterRegex = re.compile(r'(\S){8}')
    result = characterRegex.search(password)
    if result == None:
        passwordStrong = False

    alphaRegex = re.compile(r'.*[A-Z].*[a-b]|.*[a-z].*[A-Z]')
    result = alphaRegex.search(password)
    if result == None:
        passwordStrong = False

    numRegex = re.compile(r'\d+')
    result = numRegex.search(password)
    if result == None:
        passwordStrong = False

    if passwordStrong == True:
        print("Your password is strong!")
    else:
        print('''Please try again. 
    Your password needs at least one number, at least one uppercase letter, 
    at leaset one lowercase letters, and at least 8 characters''')

passwordCheck(input('Please enter your password: '))