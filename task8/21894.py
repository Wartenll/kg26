from itertools import product

cnt = 0
for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                if len({a, b, c, d}) == 4:
                    if a % 2 != b % 2 and b % 2 != c % 2 and c % 2 != d % 2:
                        cnt += 1
print(cnt)
