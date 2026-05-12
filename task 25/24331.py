def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

n, count = 13475124, 0
while count < 5:
    n += 1
    t = n
    f = []
    d = 2
    while t > 1 and len(f) < 6:
        if t % d == 0 and is_prime(d) and '5' in str(d):
            f.append(d)
            t //= d
        else:
            d += 1
    if t == 1 and len(f) == 5:
        print(n, max(f))
        count += 1