cnt = 0

for a in range(16):
    for b in range(16):
        for c in range(16):
            if a > b > c:
                cnt += 1
            for d in range(16):
                for e in range(16):
                    if a > b > c > d > e:
                        cnt += 1

print(cnt)
