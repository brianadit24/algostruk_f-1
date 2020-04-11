def mergeSort(alist):
    print('Membelah ', alist)
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
    print('Menggabungkan ', alist)

def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)


def partisi(A, awal, akhir):
    print('Bekerja pada list {}. Posisi pivot yaitu {}'.format(A, A[awal]))
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
            print('Menukar {} dengan {}'.format(A[penandaKiri], A[penandaKanan]))
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    print('Menukar {} dengan {}'.format(A[awal], A[penandaKanan]))
    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan

L = [80, 7, 24, 16, 43, 91, 35, 2, 19, 72]
L1 = L
L2 = L
print('Trace Merge Sort:')
mergeSort(L1)
print('\nTrace Quick Sort:')
quickSort(L2)