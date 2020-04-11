def mergeSort2(a):
    mergeSortBantu(a, 0, len(a) - 1)

def mergeSortBantu(a, awal, akhir):
    if awal < akhir:
        mid = (awal + (akhir - 1)) // 2
        mergeSortBantu(a, awal, mid)
        mergeSortBantu(a, mid + 1, akhir)
        pengurut(a, mid, awal, akhir)

def pengurut(a, mid, awal, akhir):
    n1 = mid - awal + 1
    n2 = akhir - mid

    separuhKiri = [a[awal + i] for i in range(n1)]
    separuhKanan = [a[mid + i + 1] for i in range(n2)]

    i = 0; j = 0; k = awal
    while i < len(separuhKiri) and j < len(separuhKanan):
        if separuhKiri[i] < separuhKanan[j]:
            a[k] = separuhKiri[i]
            i += 1
        else:
            a[k] = separuhKanan[j]
            j += 1
        k += 1

    while i < n1:
        a[k] = separuhKiri[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = separuhKanan[j]
        j += 1
        k += 1
    
# list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# mergeSort2(list1)
# print(list1)
    