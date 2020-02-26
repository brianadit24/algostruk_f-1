def gambarlahPersegiEmpat(a, b):
    assert a >= 0
    assert b >= 0
    for i in range(a):
        for x in range(b):
            if i == 0 or i == a - 1 or x == 0 or x == b - 1:
                print("@", end = " ")
            else:
                print(" ", end = " ")
        print()

gambarlahPersegiEmpat(4,5)
