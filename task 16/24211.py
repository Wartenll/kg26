from functools import lru_cache

def F(n):
    # Добавляем проверку для отрицательных значений
    if n - 2 < 0:
        return 3 * (G(0) + 5)  # или другое базовое значение
    return 3 * (G(n - 2) + 5)

@lru_cache(None)
def G(n):
    if n < 8:
        return 3 * n
    return G(n - 3) + 2

# Предварительно вычисляем все значения G
for i in range(0, 12_345 + 1):
    G(i)

# Вычисляем F
result = F(12_345)
print(result)