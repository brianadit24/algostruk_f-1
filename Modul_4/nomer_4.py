from mhsTIF import *

def cariKurang(daftar):
    for i in daftar:
        if i.uangSaku < 250000:
            print(i)

cariKurang(Daftar)