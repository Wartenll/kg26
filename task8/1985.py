from itertools import permutations

alph1 = 'АИОУ'
alph2 = 'БКЛН'
cnt=0
for val in permutations('АБИКОЛУН'):
    if all((val[i] in alph1) != (val[i+1] in alph1) for i in range(7)):
        cnt += 1

print(cnt)