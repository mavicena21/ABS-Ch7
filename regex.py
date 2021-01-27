import re
nohp = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = nohp.search('My number is 415-555-4242')
print('Phonenumber found: ' + mo.group())

nohp2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = nohp2.search('Nomor aing adalah 555-666-6969')
print(mo2.group(1))
print(mo2.group(2))
print(mo2.group(0))