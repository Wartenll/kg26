from math import *

Vs = 3 * 2 ** 23  # bit
hw = 1600 * 1200
N = 1024
i_c = ceil(log2(N))
Vi = 1.2 * Vs
i = floor(Vi / hw)
print(i - i_c)
