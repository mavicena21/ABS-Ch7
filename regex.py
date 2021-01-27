import re
nohp = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = nohp.search('My number is 415-555-4242')
print('Phonenumber found: ' + mo.group())

nohp2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = nohp2.search('Nomor aing adalah 555-666-6969')
print(mo2.group(1))
print(mo2.group(2))
print(mo2.group(0))


a, b = mo2.groups()
print(a)
print(b)
print(mo2.groups())

nohp3 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo3 = nohp3.search('Nomor hpku adalah (415) 555-4242')
print(mo3.group(1))
print(mo3.group(2))

#matching multiple groups with the pipe
haha = re.compile(r'Batman|Superman')
mo4 = haha.search('Batman dan Superman')
mo5 = haha.search('Superman dan Batman')
print(mo4.group())
print(mo5.group())

batregex = re.compile(r'Bat(man|mobile|copter|bat)')
mo6 = batregex.search('Batmobile lost a wheel when fighting with Batbat')
print(mo6.group())
print(mo6.group(1))