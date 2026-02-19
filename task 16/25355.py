from functools import lru_cache

def F(n):
    if n >= 19:
        return F(n - 4) + 3580

    if n - 7 < 0:
        return 6 * (G(0) - 36)
    return 6 * (G(n - 7) - 36)

@lru_cache(None)
def G(n):
    if n >= 248_045:
        return n / 20 + 28
    return G(n + 9) - 4

for i in range(250_000, -1, -1):
    G(i)

result = F(673)
print(result)