# phoneAndEmail.py - find phone numbers and email addresses on the clipboard

import pyperclip, re 

### SAMPLE CLIPBOARD TEXT ###
# dog@the.com
# 435-348-0223
# Ahphabet soiur id gestg adfjaskh
# me@mail.com, (598)9049432 claim@business.net


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?               # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)?                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
([a-zA-Z0-9._%+-]+)                    #username
(@)                                    #@ symbol
([a-zA-Z0-9.-]+)                       #domain name
([a-zA-Z]{2,4})                        #TLD (.something)
)''', re.VERBOSE)

text = str(pyperclip.paste())
phoneMatches = phoneRegex.findall(text)
emailMatches = emailRegex.findall(text)
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3],groups[5]])
    if groups[8] != "":
        phoneNum += 'x'+ groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to the clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses were found.')


