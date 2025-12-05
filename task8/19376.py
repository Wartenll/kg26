from itertools import product
cnt =0
for val in product('ПСКАЛЬ', repeat = 4):
    val=''.join(val)
    if val[0] != 'Ь' and val.count('ЬЬ')== 0:
        cnt += 1
print(cnt)