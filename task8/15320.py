from itertools import product

alph = 'АПРСУ'
cnt = 0

for val in product(alph, repeat=5):
    val = ''.join(val)
    cnt += 1

    if val.count('У') > 1:
        continue

    if 'АА' in val:
        continue

    print(cnt)
    break
