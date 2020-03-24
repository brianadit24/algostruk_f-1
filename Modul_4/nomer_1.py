from mhsTIF import *

def cariIndex(daftar, target):
    index = []
    for i in range(len(daftar)):
        if daftar[i].kota == target:
            index.append(i)
    return index

print(cariIndex(Daftar, 'Klaten'))
