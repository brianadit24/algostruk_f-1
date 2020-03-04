from mahasiswa import Mahasiswa

mhs9 = Mahasiswa('Maul', 3234234, 'Cirebon', 20000)
mhs9.ambilKuliah('Cyber Security')
mhs9.ambilKuliah('Cryptography')
mhs9.ambilKuliah('Networking')
print(mhs9.listKuliah)
mhs9.hapusKuliah('Networking')
print(mhs9.listKuliah)
