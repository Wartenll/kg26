
from itertools import product
alph = sorted('АЕКНС')
cnt = 0
for pos, val in enumerate(product(repeat=6), start=1):
    val = ''.join(val)
    cnt += 1
print(cnt)
from itertools import product
cnt =0
for pos, val in product(sorted('АЕКНС'),start=1, repeat = 5):
    val=''.join(val)
    if val.count('Г')==1 and val[0] != 'А' and val [-1] != 'Е':
        cnt += 1
print(cnt)