from time import time as detak
from random import shuffle as kocok
from latihan import *

k = [i for i in range(1, 6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]
u_mrg = k[:]
u_qck = k[:]
aw = detak();bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw))
aw = detak();selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw))
aw = detak();insertionSort(u_ins);ak=detak();print('insertion: %g detik' %(ak-aw))
aw = detak();mergeSort(u_mrg);ak=detak();print('merge: %g detik' %(ak-aw))
aw = detak();quickSort(u_qck);ak=detak();print('quick: %g detik' %(ak-aw))

# bubble: 7.7148 detik
# selection: 2.27662 detik
# insertion: 3.73162 detik
# merge: 0.046541 detik
# quick: 0.0423257 detik