from itertools import product, permutations

def f(x, y, z, w):
    return ((w <= y) <= x) or not z

for i in product((0, 1), repeat=7):
    table = [
        (i[0], i[1],1,i[2]),
        (i[3],0,i[4],i[5]),
        (i[6],1,0,0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, t))) for t in table] == [0,0,0]:
                print(*p, sep='')
                break