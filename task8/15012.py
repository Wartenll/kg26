from itertools import product
from string import printable

cnt = 0

for val in product(printable[:14], repeat=5):
    val = ''.join(val)
    if  val[0] != '0' and (val[4] == '0' or val[4] == '3'):
        

