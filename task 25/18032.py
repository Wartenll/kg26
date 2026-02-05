def f(n):
    total = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

result = []
for num in range(1000, 10000):
    s = sum_of_divisors(num)
    if s % 100 == 23:
        result.append((num, s))

result.sort()

for num, s in result:
    print(f"{num} {s}")