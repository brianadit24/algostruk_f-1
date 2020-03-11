m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2,3],[1,3,4],[1,4,3]]

m3 = [[1,2,3],[1,2,5]]
m4 = [[3,4,5],[1,2,3],[2,1,'5']]

def cekMatrix(matrix):
    hitung = 0
    if len(matrix) != len(matrix[0]):
        print('Matriks haruslah bujur sangkar')
        return
    for i in range(len(matrix)):
        cek = all(isinstance(x, int) for x in matrix[i])
        if cek == True:
            hitung += 1
    if hitung == 3:
        print('Matriks bujur sangkar dan memiliki tipe yang konsisten')
    else:
        print('Matriks memiliki tipe yang tidak konsisten')

def ukurMatrix(matrix):
    ukurBaris = len(matrix)
    ukurKolom = len(matrix[0])
    print('Matriks tersebut adalah matriks berukuran {}x{}'.format(ukurBaris, ukurKolom))

def penjumlahanMatrix(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        print('Ukuran matriks tidak sama')
        return

    jumlah = [[0 for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2)):
            jumlah[i][j] = matrix1[i][j] + matrix2[i][j]

    for i in jumlah:
        print(i)

def perkalianMatrix(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        print('Ukuran matriks tidak sesuai')
        return

    kali = [[0 for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            for k in range(len(matrix1)):
                kali[i][j] += matrix1[i][k] * matrix2[k][j]
    
    for i in kali:
        print(i)

def determinanMatrix(matrix):
    if len(matrix) != len(matrix[0]):
        print('Matriks harus bujur sangkar')
        return

    tambah = [1 for i in range(len(matrix))]
    kurang = [1 for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix) - 1):
            matrix[i].append(matrix[i][j])

    matrix2 = matrix.copy()

    for i in range(len(matrix2)):
        matrix2[i] = list(reversed(matrix2[i]))

    nilai = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            tambah[i] *= matrix[j][j + nilai]
            kurang[i] *= matrix2[j][j + nilai]
        nilai += 1

    kurang = [-x for x in kurang]
    determinan = sum(tambah) + sum(kurang)

    return determinan

cekMatrix(m1)
cekMatrix(m3)
cekMatrix(m4)
ukurMatrix(m1)
print()
penjumlahanMatrix(m1, m2)
print()
perkalianMatrix(m1, m2)
print()
print(determinanMatrix(m2))
