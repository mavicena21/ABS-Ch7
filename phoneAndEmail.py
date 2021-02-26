import pyperclip, re
# regex hp

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? #3 first digit
(\s|-|\.)? #separator 
(\d{3}) #tiga digit tengah
(\s|-|\.) #empat digit terakhir
(\s*(ext|x|ext.)\s*(\d{3,5}))? #extension
)''', re.VERBOSE)

# regex email
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+#username
@#simbol @
[a-zA-Z0-9.-]+#domain
(\.[a-zA-Z]{2,4})#dotsomething
)''', re.VERBOSE)

#cari teks yang cocok di clipboard
text = str(pyperclip.paste)
print(text)
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copy result
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('gak ada nope atau email')