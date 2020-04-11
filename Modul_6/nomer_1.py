from mhsTIF import *

def mergeSortMahasiswa(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        separuhKiri = alist[:mid]
        separuhKanan = alist[mid:]

        mergeSortMahasiswa(separuhKiri)
        mergeSortMahasiswa(separuhKanan)

        i = 0
        j = 0
        k = 0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i].NIM < separuhKanan[j].NIM:
                alist[k] = separuhKiri[i]
                i += 1
            else:
                alist[k] = separuhKanan[j]
                j += 1
            k += 1

        while i < len(separuhKiri):
            alist[k] = separuhKiri[i]
            i += 1
            k += 1

        while j < len(separuhKanan):
            alist[k] = separuhKanan[j]
            j += 1
            k += 1

def quickSortMahasiswa(A):
    quickSortBantu(A, 0, len(A) - 1)

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)


def partisi(A, awal, akhir):
    nilaiPivot = A[awal].NIM

    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:
        while penandaKiri <= penandaKanan and A[penandaKiri].NIM <= nilaiPivot:
            penandaKiri += 1
        
        while penandaKanan >= penandaKiri and A[penandaKanan].NIM >= nilaiPivot:
            penandaKanan -= 1

        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan

def cetakObjekMhs(A):
    for i in A:
        print(i)

list1 = Daftar
list2 = Daftar

mergeSortMahasiswa(list1)
print('Hasil dari Merge Sort:\n')
cetakObjekMhs(list1)
quickSortMahasiswa(list2)
print('Hasil dari Quick Sort:\n')
cetakObjekMhs(list2)