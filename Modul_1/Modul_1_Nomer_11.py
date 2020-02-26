def apakahKabisat(tahun):
    if tahun % 4 == 0 or tahun % 400 == 0 and tahun % 100 != 0:
        return True
    else:
        return False

print(apakahKabisat(1896))