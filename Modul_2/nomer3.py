from mahasiswa import Mahasiswa

print('Program untuk memasukan mahasiswa baru')
nama = input('Masukan Nama: ')
NIM = int(input('Masukan NIM: '))
kota = input('Masukan Kota: ')
uangSaku = int(input('Masukan uang saku: '))

mhs = Mahasiswa(nama, NIM, kota, uangSaku)
print('\nAnda telah menginput data Mahasiswa sebagai berikut: \n')
print(mhs)
