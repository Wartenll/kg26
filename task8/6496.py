from itertools import product

alph = 'БЕРСК'
count = 0
for R in range(5, 8):
    for val in product(alph, repeat=R):
        val = ''.join(val)
        count += 1
print(count)
