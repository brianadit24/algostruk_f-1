from latihan import mergeSort, quickSort
from time import time as detak
from random import shuffle as kocok
from nomer_5 import mergeSort2
from nomer_6 import quickSort2

k = [i for i in range(1, 6001)]
kocok(k)
u_mrg = k[:]
u_qck = k[:]
u_mrg2 = k[:]
u_qck2 = k[:]

aw = detak();mergeSort(u_mrg);ak=detak();print('merge: %g detik' %(ak-aw))
aw = detak();quickSort(u_qck);ak=detak();print('quick: %g detik' %(ak-aw))
aw = detak();mergeSort2(u_mrg2);ak=detak();print('merge tanpa slice: %g detik' %(ak-aw))
aw = detak();quickSort2(u_qck2);ak=detak();print('quick median 3: %g detik' %(ak-aw))

# merge: 0.0935357 detik
# quick: 0.0298665 detik
# merge tanpa slice: 0.0710406 detik
# quick median 3: 0.0286579 detik