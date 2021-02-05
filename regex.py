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

#matching zero or more with the star
asterisku = re.compile(r'Bat(wo)*man')
an = asterisku.search('The adventures of Batman')
an1 = asterisku.search('The adventures of Batwoman')
an2 = asterisku.search(('The adventures of Batwowowowoman'))
print(an.group())
print(an1.group())
print(an2.group())

#matching one or more with the plus
supermanto = re.compile(r'Super(wo)+man')
so1 = supermanto.search('The adventures of Superman')
so2 = supermanto.search('The adventures of Superwoman')
so3 = supermanto.search('The adventures of Superwowowowoman')
print(so1 == None)
print(so2.group())
print(so3.group())

#matching specific repetitions with curly brackets
haregex = re.compile(r'(Ha){3}')
ha1 = haregex.search('HaHaHa')
ha2 = haregex.search('HaHa')
print(ha1.group())
print(ha2 == None)

#greedy matching and non greedy matching
greedyregex = re.compile(r'(Ha){3,5}')
gre1 = greedyregex.search('HaHaHaHaHa')

nongreedyregex = re.compile(r'(Ha){3,5}?')
nongre1 = nongreedyregex.search('HaHaHaHaHaHaHa')

print(gre1)
print(nongre1)

#search() method vs findall() method
ss = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
ss1 = ss.search('Cell: 415-555-9999 Work: 212-555-0000')
mm = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mm1 = mm.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(ss1.group())
print(mm1)

#matching evertyhing with dot-star
nameregex = re.compile(r'First Name: (.*) Last Name: (.*)')
ya = nameregex.search('First Name: Al Last Name: Sweigart')
print(ya.group(1))
print(ya.group(2))

#non greedy dot star
ngdstar = re.compile(r'<.*?>')
ngd1 = ngdstar.search('<To serve man> for dinner>')

gdstar = re.compile(r'<.*>')
ngd2 = gdstar.search('<To serve man> for dinner,>')
print(ngd1.group())
print(ngd2.group())