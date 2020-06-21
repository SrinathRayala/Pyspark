import re
phoneRegex=re.compile(r'''
(((\d\d\d)|(\(\d\d\d\)))? # Optional
(\s|-)
\d\d\d
-
\d\d\d\d
(((ext(\.)?\s)|x)
 (\d{2,5}))?)
''',re.VERBOSE)
emailRegex=re.compile(r'''
[A-Za-z0-9_.+]+
@
[A-Za-z0-9_.+]+
''',re.VERBOSE)
text='345-134-2433asdjeoujalasdfadf 534-434-3455 sadfaaf 543-345-3454 wf'
#message='call me 439-443-5342 tomorrow'
#mo=phoneNumber.search(message)
#print(mo.group())
extractPhone=phoneRegex.findall(text)
extractEmail=emailRegex.findall(text)
allPhones = []
for phoneNumber in extractPhone:
    allPhones.append(phoneNumber[0])
results='\n'.join(allPhones)+'\n'+'\n'.join(extractEmail)
print(results)
#print(allPhones)
#print(extractEmail)