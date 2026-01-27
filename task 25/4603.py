from fnmatch import fnmatch



for N in range(12347 -12347 % 141, 10 ** 8 + 1, 141):
    if fnmatch(str(N), '1234*7') and N % 141 == 0:
        print(N, N // 141)
############################################################
from itertools import product
from string import printable

ans=[]
for V in printable[::10]:
    for l in range(0,3):
        for Z in product(printable[:10], repeat = l):
            num = int(f'12{''.join(Z)}4{V}65')
            if num % 161 == 0:
                ans.append([num,num // 161])
for i in sorted(ans):
        print(*1)

