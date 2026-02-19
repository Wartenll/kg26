def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d.add(i)
            d.add(num // i)
    return sorted(d)

for N in range(500_001, 10 ** 20):
    divisors = f(N)
    # Дальше нужно дописать условие задачи
    # Например, проверка на что-то
    if len(divisors) > 0:  # пример условия
        print(N, divisors)
        break