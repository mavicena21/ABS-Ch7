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

#optional matching with the question mark
batwomantol = re.compile(r'Bat(wo)?man')
mo7 = batwomantol.search('The Adventures of Batman')
print(mo7.group())

mo8 = batwomantol.search('The Advetures of Batwoman')
print(mo8.group())

#contoh question mark dalam no hp
fontolregex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo9 = fontolregex.search('Nomor hpku adalah 415-555-4242')
print(mo9.group())
mo10 = fontolregex.search('Nomor hpku adalah 555-42424')
print(mo10.group())