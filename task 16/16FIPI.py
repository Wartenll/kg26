from functools import lru_cache


@lru_cache(None)
def F(n):
    if n <10:
        return n
    return (F(247563)/519-477*F(247560))/ F(247557)


print((F(2000) - 2 * (F(2002) + F(2003))) / F(2004))
