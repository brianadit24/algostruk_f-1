from mhsTIF import *

# def cariUangSakuTerkecil(daftar):
#     uangSaku = []
#     for i in daftar:
#         uangSaku.append(i.uangSaku)
#     return min(uangSaku)

# print(cariUangSakuTerkecil(Daftar))

def cariTerkecil(daftar):
    terkecil = daftar[0].uangSaku
    for i in daftar:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku
    return terkecil

print(cariTerkecil(Daftar))