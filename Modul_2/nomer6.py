from manusia import Manusia

class SiswaSMA(Manusia):
    def __init__(self, nama, kota, jurusan):
        Manusia.__init__(self, nama)
        self.kota = kota
        self.jurusan = jurusan

    def __str__(self):
        return 'Nama : {} \nJurusan : {} \nKota : {}'.format(self.nama, self.jurusan, self.kota)

    def tampilkanNama(self):
        print('Nama siswa : {}'.format(self.nama))

    def tampilkanJurusan(self):
        print('Siswa dengan nama {} memilih jurusan {}'.format(self.nama, self.jurusan))

    def tampilkanKota(self):
        print('Siswa dengan nama {} tinggal di {}'.format(self.nama, self.kota))

    def makanSiang(self, makanan):
        print('{} makan {} di kantin dengan keadaan {}'.format(self.nama, makanan, self.keadaan))
        self.keadaan = 'Kenyang'

siswa = SiswaSMA('Bobi', 'Solo', 'IPS')
siswa.tampilkanJurusan()
siswa.tampilkanKota()
siswa.olahraga('paralayang')
siswa.makanSiang('seblak')