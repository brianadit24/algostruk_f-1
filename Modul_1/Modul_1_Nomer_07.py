from math import sqrt as sq

def faktorPrima(n):
    assert n >= 0
    hasil = []
    while n % 2 == 0: 
        hasil.append(2)
        n = n / 2
    for i in range(3,int(sq(n))+1,2): 
        while n % i== 0: 
            hasil.append(i)
            n = n / i 
    if n > 2: 
        hasil.append(int(n)) 

    return hasil
  
print(faktorPrima(120))