from itertools import product, permutations


def f(x, y, z, w):
    return (x <= y) and z and not w


for i in product((0, 1), repeat=7):
    table = [
        (0, 1, i[0], i[1]),
        (1, 1, i[3], i[4]),
        (1, i[5], 1, i[6])
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1,1,1]:
                print(*p, sep='')
