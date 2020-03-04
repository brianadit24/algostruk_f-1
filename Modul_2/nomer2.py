from mahasiswa import Mahasiswa

mhs = Mahasiswa('Abdul', 1212213, 'Jakarta', 270000)
# a
print(mhs.ambilKotaTinggal())

#b
mhs.perbaruiKotaTinggal('Surabaya')
print(mhs.ambilKotaTinggal())

#c
print(mhs.ambilUangSaku())
mhs.tambahUangSaku(50000)
print(mhs.ambilUangSaku())
