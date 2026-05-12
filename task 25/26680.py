def fact_3(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i <= num:  # Исправил: должно быть <= вместо <
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:  # Или if num > 1: (так как 1 не простое)
        d += [num]

    return d