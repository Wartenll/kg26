max_R = 0
for N in range(1, 30):
    b = bin(N)[2:]
    s = sum(int(d) for d in b)
    if s % 2 == 0:
        R = int("10" + b[:-2] + "00" if len(b) >= 2 else "1000", 2)
    else:
        R = int("11" + b[:-2] + "11" if len(b) >= 2 else "1111", 2)
    max_R = max(max_R, R)
print(max_R)