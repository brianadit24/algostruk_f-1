def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1

    index = []

    while low <= high:
        mid = (high+low) // 2
        if kumpulan[mid] == target:
            while kumpulan[mid - 1] == target:
                mid -= 1
            while kumpulan[mid] == target:
                index.append(mid)
                mid += 1
                if mid > len(kumpulan)-1:
                    break
            return index
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return 'False'

a = [1,1,1,2,3,4]
b = [1,2,4,4,4,4]
c = [2,3,5,6,6,6,8,9,9,10]
print(binSe(a,1))
print(binSe(b,4))
print(binSe(c, 6))