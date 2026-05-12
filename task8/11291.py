from itertools import product

count = 0
for d in product('012345', repeat=6):
    s = ''.join(d)
    if s.count('2') == 1:
        p = s.index('2')
        if (p == 0 or int(s[p-1]) % 2 == 1) and (p == 5 or int(s[p+1]) % 2 == 1):
            count += 1

print(count)