def swap(kumpulan, ele1, ele2):
    temp = kumpulan[ele1]
    kumpulan[ele1] = kumpulan[ele2]
    kumpulan[ele2] = temp
    return kumpulan

def cariYangTerkecil(kumpulan, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini + 1, sampaiSini):
        if kumpulan[i] < kumpulan[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

def bubbleSort(kumpulan):
    n = len(kumpulan)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if kumpulan[j] > kumpulan[j + 1]:
                swap(kumpulan, j, j + 1)
    return kumpulan

def selectionSort(kumpulan):
    n = len(kumpulan)
    for i in range(n - 1):
        indexKecil = cariYangTerkecil(kumpulan, i, n)
        if indexKecil != i:
            swap(kumpulan, i, indexKecil)
    return kumpulan

def insertionSort(kumpulan):
    n = len(kumpulan)
    for i in range(1, n):
        nilai = kumpulan[i]
        pos = i
        while pos > 0 and nilai < kumpulan[pos - 1]:
            kumpulan[pos] = kumpulan[pos - 1]
            pos = pos - 1
        kumpulan[pos] = nilai
    return kumpulan

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        separuhKiri = alist[:mid]
        separuhKanan = alist[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i = 0
        j = 0
        k = 0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
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

def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)


def partisi(A, awal, akhir):
    nilaiPivot = A[awal]

    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:
        while penandaKiri <= penandaKanan and A[penandaKiri] <= nilaiPivot:
            penandaKiri += 1
        
        while penandaKanan >= penandaKiri and A[penandaKanan] >= nilaiPivot:
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