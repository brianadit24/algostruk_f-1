class Pesan:
    def __init__(self, sebuahString):
        self.teks = sebuahString

    def cetakIni(self):
        print(self.teks)

    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))

    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))

    def jumKar(self):
        return len(self.teks)

    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai {} karakter'.format(len(self.teks)))

    def perbarui(self, stringBaru):
        self.teks = stringBaru

    def apakahTerkandung(self, kata):
        if kata in self.teks:
            return True
        else:
            return False

    def hitungKonsonan(self):
        konsonan = 'bcdfghjklmnpqrstvwxyz'
        kata2 = str.lower(self.teks)
        count = 0
        for i in kata2:
            if i in konsonan:
                count += 1
        return count

    def hitungVokal(self):
        vokal = 'aiueo'
        kata2 = str.lower(self.teks)
        count = 0
        for i in kata2:
            if i in vokal:
                count += 1
        return count
        
# a
p9 = Pesan('Indonesia adalah negeri yang indah')
print(p9.apakahTerkandung('ege'))
print(p9.apakahTerkandung('eka'))

# # b
p10 = Pesan('Surakarta')
print(p10.hitungKonsonan())

#c
print(p10.hitungVokal())

