def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    for i in sorted(d):
        if i % 10 == 7 and i != 7:
            return i
    return 0


for N in range(500_001, 10 ** 20):
    result = f(N)
    if result > 0:
        print(N, result)
        break