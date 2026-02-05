def M(num):
    d = [i for i in range(2, int(num ** 0.5) + 1) if num % i == 0]
    if not d: return 0
    return min(d) + max(d) if num > 1 and max(d) != num else min(d) + n // min(d)


c = 0
n = 800001
while c < 5:
    m = M(n)
    if m % 10 == 4:
        print(n, m)
        c += 1
    n += 1
