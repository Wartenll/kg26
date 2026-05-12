from math import *

for N in range(1, 10 ** 10):
    i = ceil(log(N))
    I = ceil(i * 2783 / 8)
    if I * 62_784 >= 356 * 2 ** 20:
        print(N)
        break
