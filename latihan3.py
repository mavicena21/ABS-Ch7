tamu = {'budi': {'apel': 4, 'pisang': 5},
        'jono': {'apel': 2, 'pisang': 4}}
def dikto(nama, item):
    totalitem = 0
    for k, v in nama.items():
        totalitem = totalitem + v.get(item, 0)
    return totalitem
print('Jumlah barang')
print('apel ' + str(dikto(tamu, 'apel')))
print('pisang ' + str(dikto(tamu, 'pisang')))

stuff = {'g': 1000, 's': 30, 'b': 50}
def totalbarang(inven):
    totalstuff = 0
    for k, v in inven.items():
        print(str(v) + ' ' + str(k))
    totalstuff = totalstuff + 1
    print('jumlah barang' + str(totalstuff))

def tambahloot(inven, loot):
    for i in loot:
        inven.setdefault(i, 0)
        inven[i] += 1
    return inven
dragonloot = ['g', 'g', 'g', 'g', 's', 's', 's', 'b', 'b', 'b']
stuff = tambahloot(stuff, dragonloot)
totalbarang(stuff)

#contoh else statement
print('masukkan nama')
name = input()
if name == 'jojo':
    print('hello jojo')
else:
    print('hello stranger')