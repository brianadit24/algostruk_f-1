def mergeSort(alist):
    print('Membelah', alist)
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
    print('Menggabungkan', alist)

list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(list1)
print(list1)