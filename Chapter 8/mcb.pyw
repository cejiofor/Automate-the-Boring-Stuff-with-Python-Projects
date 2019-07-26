#! python3
# mcb.py
# Multiclipboard Project by Christopher Ejiofor
# Saves and loads pieces of text to the clipboard

import os, sys, pyperclip, shelve

# Project Requirements
    # py mcb.pyw save <keyword> - To save clipboard text to a keyword using
    # py mcb.pyw <keyword> - To load clipboard text saved to keyword 
    # py mcb.pyw list - To copy a list of keywords to the clipboard
    # 
    # check command line arguement for the keyword
    # if save - clipboard contents are saved to the keyword
    # if list - all the keywords are copied to clipboard
    # otherwise - text of keyword is  
#

mcbShelf = shelve.open('mcb')

cmdArgs = sys.argv.copy()
if (len(cmdArgs) == 3):
    if (cmdArgs[1] == 'save'):
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif (cmdArgs[1] == 'delete'):
        del mcbShelf[sys.argv[2]]
elif(len(cmdArgs) == 2):
    if(cmdArgs[1] == "list"):
        # keywords = "\n"
        keywords = str(list(mcbShelf.keys()))
        pyperclip.copy(keywords)
    elif(cmdArgs[1] == "delete"):
        for key in mcbShelf:
            del mcbShelf[key]
    elif (cmdArgs[1] in mcbShelf):
        pyperclip.copy(mcbShelf[cmdArgs[1]])
    else:
        raise Exception ("Keyword does not exists")

mcbShelf.close()
