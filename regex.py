import re
nohp = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = nohp.search('My number is 415-555-4242')
print('Phonenumber found: ' + mo.group())