from itertools import product
alph=['АВОРТА']
for pos, val in enumerate(product(repeat=4), start=1):
    val = ''.join(val)


