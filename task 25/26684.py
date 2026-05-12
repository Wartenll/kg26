def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i < num + 1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 2:
        d += [num]
    return d


cnt = 0
for N in range(5_000_000 + 1, 10 ** 20):
    d = fact(N)
    if any(d.count(i) == 5 for i in set(d)):
        print(N, min(i for i in set(d) if d.count(i) == 3))
        cnt+=1
        if cnt == 5:
            break
