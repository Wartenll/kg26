from functools import lru_cache

def G(n):
    while n <= 303728:
        n += 8
    return n - 15

@lru_cache(None)
def F(n):
    if n >= 128:
        return F(n - 5) + 1092
    return 5 * G(n - 7) + 29

print(F(2049))