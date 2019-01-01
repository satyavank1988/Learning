import re


message = 'Call me 999-052-2251 tomorrow or at 773-838-2557'
message1 = 'Call me (999)-052-225 tomorrow or at 773-838-255'


phoneNumRegex  = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
pNR = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
try:
    mo2 = pNR.search(message1)
    print mo2.group()
except:
    print "none type error"


mo = phoneNumRegex.search(message)   # this will search one occurance of phone number
mo1 = phoneNumRegex.findall(message)  # this will search all occurrance of phone
print mo.group()
print mo1

