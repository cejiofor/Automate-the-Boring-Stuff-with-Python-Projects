##! python3
#regexStrip.py - a function that takes a string and mimics the strip() string method

#If no other arguments are passed, whitespace characters are removed
#If there is a second argument, the characters specified will be removed from the string


import re, sys

def regexStrip(str, char=""):
    if char == "":
        spaceReg = re.compile(r'\s')
        newString = re.sub(spaceReg, "", str)
    else:
        replRegex = re.compile(fr'{char}', re.I)
        newString = re.sub(replRegex, "", str)
    print(newString)


#TODO break up string and char arugements into a list of characters
#TODO Loop thorough both lists, removing each str element matching an element in char list
#TODO join  str element together with no spaces and return new string

regexStrip('This is Sparta! VERB ADJECTIVE')
regexStrip('This is Sparta! VERB ADJECTIVE', "I")
