from itertools import product

alph = sorted('КРАТЕР')
cnt = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val=''.join(val)
    if val[0]
