from itertools import product

alph = 'А,О'
cnt = 0

for word in product('МАСЛО', repeat=6):
    if sum(1 for val in word if val in alph) == 1:
        cnt += 1

print(cnt)