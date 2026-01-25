from string import printable
from itertools import permutations

cnt = 0
for val in permutations(printable[:8], r=6):
    val = ''.join(val)
    if (val.count('и')+ val.count ('о') + val.count('е')) == 2:
        for i in range (4):
            if sum(1 for i in range(4) if val[i] == 'тихо'[i]) == 2:
                cnt += 1
print(cnt)