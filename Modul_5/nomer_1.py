from mhsTIF import *

def urutkanNIM(kumpulan):
    n = len(kumpulan)
    for i in range(1, n):
        nilai = kumpulan[i]
        pos = i
        while pos > 0 and nilai.NIM < kumpulan[pos - 1].NIM:
            kumpulan[pos] = kumpulan[pos - 1]
            pos = pos - 1
        kumpulan[pos] = nilai
    
    for i in kumpulan:
        print(i)

urutkanNIM(Daftar)