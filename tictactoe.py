# tictactoe
thepapan = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' ',}
def printpapan(papan):
    print(papan['1'] + '|' + papan['2'] + '|' + papan['3'])
    print('-+-+-')
    print(papan['4'] + '|' + papan['5'] + '|' + papan['6'])
    print('-+-+-')
    print(papan['7'] + '|' + papan['8'] + '|' + papan['9'])
turn = 'X'
for i in range(9):
    printpapan(thepapan)
    print('Giliran untuk ' + turn + ' mau melangkah di kotak mana?')
    move = input()
    thepapan[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'