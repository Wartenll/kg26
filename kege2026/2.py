from itertools import product, permutations


def f(x, y, w, z):
    return (z <= y) and ((w <= x) <= y)


for i in product((0, 1), repeat=7):
    table = [
        (i[0], 0, 0, i[1]),
        (i[2], i[3], 1, i[4]),
        (i[5], 1, 1, 1)
    ]

