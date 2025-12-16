from itertools import product

alph = sorted('БМЮРН')
cnt = 0
for pos, val in enumerate(product(repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 == 1 and val.count('Р') >= 2 and 'Ю' not in val:
        cnt += 1

print(pos)
