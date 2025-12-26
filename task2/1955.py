from itertools import product, permutations


def f(x, y, w, z):
    return not(y <=(x==w)) and (z<=x)
for i in product((0,1), repeat=7):
    table=[
        (i[0], 1,1,i[1]),
        (0,i[3],i[4],0),
        (i[5],0,1,0,)
    ]
if len (table) == len(set(table)):
    for p in permutations('xywz'):
        if [f(**dict(zip(p,t))) for t in table] == [0,0,0]:
            print(*p, sep='')