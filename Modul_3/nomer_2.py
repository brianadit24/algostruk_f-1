def buatNol(m, n = None):
    if n == None:
        n = m

    matrix = [[0 for j in range(n)] for i in range(m)]

    for i in matrix:
        print(i)

def buatIdentitas(m):
    matrix = [[ 1 if j == i else 0 for j in range(m)] for i in range(m)]

    for i in matrix:
        print(i)

buatNol(3)
print()
buatIdentitas(6)