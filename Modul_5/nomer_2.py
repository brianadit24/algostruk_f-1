def gabungkan(l1, l2):
    la = len(l1); lb = len(l2)
    
    l3 = []

    i = 0; j = 0

    while i < la and j < lb:
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1
    
    while i < la:
        l3.append(l1[i])
        i += 1
    
    while j < lb:
        l3.append(l2[j])
        j += 1

    return l3

l1 = [1, 3, 4, 7]
l2 = [0, 2, 5, 6, 8, 9]

print(gabungkan(l1, l2))