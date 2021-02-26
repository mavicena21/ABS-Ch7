import re
regox = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
yaw = regox.search('contact me 089-0033-9482')
print(yaw.group())
qm = re.compile(r'bat(wo)?man')
qm1 = qm.search('adventore of batman')
qm2 = qm.search('adventore of batwoman')
print(qm1.group())
print(qm2.group())
tikitakatoe = {'1': ' ', '2': ' ', '3': ' ',
               '4': ' ', '5': ' ', '6': ' ',
               '7': ' ', '8': ' ', '9': ' ',}
def printpapan(namaboard):
    print(namaboard['1'] + '|' + namaboard['2'] + '|' + namaboard['3'])
    print('_+_+_')
    print(namaboard['4'] + '|' + namaboard['5'] + '|' + namaboard['6'])
    print('_+_+_')
    print(namaboard['7'] + '|' + namaboard['8'] + '|' + namaboard['9'])
turn = 'X'
for i in range(9):
    print('Tiki Taka Toe')
    printpapan(tikitakatoe)
    print('mau gerak di kotak mana? (1-9)')
    move = input()
    tikitakatoe[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printpapan(tikitakatoe)