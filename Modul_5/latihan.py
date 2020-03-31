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

list1 = [13, 18, 44, 25, 66, 107, 78, 89]

# print(cariYangTerkecil(list1, 0, len(list1)))
# print(swap(list1, 0, 2))
# print(bubbleSort(list1))
# print(selectionSort(list1))
# print(insertionSort(list1))