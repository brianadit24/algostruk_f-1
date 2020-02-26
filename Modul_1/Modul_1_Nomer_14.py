def formatRupiah(angka):
    assert angka >= 0
    konversi = 'Rp {0:,}'.format(angka)
    konversi = konversi.replace(',' , '.')
    return konversi

print(formatRupiah(1500))