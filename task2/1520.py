from itertools import product, permutations


def f(a,b,c):
    return (a<=b) and (a and b <= c)
table=[
            (0,0,0),
            (0,1,0),
            (0,1,0),
            (0,1,1),
            (1,0,0),
            (1,0,1),
            (1,1,0),
            (1,1,1)
    ]
if len (table) == len(set(table)):
    for p in permutations('a,b,c'):
        if [f(**dict(zip(p,t))) for t in table] == [1,0,1,1,1,0,1]:
            print(*p, sep='')