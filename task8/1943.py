from itertools import product
cnt =0
for val in product('ЗЕРКАЛО', repeat =6):
    val=''.join(val)
    if 1<= val.count('К')<=4:
        for i in 'ЗЕРКАЛО':
            if val.count(i) > 1:
                break
        else:
            cnt += 1
print(cnt)