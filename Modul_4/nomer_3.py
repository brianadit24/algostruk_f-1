from mhsTIF import *

def cariTerkecil(daftar):
    terkecil = daftar[0].uangSaku
    for i in daftar:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku

    for i in daftar:
        if i.uangSaku == terkecil:
            print(i)

cariTerkecil(Daftar)