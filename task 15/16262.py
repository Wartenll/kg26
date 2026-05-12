from itertools import combinations


def f(x,y):
    A = A1 <= x <= A2
    A = A1 <= y <= A2
    return ((A<x) or (x**2 - 7 * x + 10 > 0)) and (( A >= y) or(y**2 + 7*y + 12))
line = [x for  x in range(0, 100) for eps in (0,0.1,0,9)]
line = [y for  y in range(0, 100) for eps in (0,0.1,0,9)]
ans =[]
for A1,A2 in combinations(line, 2):
    if all(f(x, y) for x in line):
        if all(f(y,x) for y in line):
            ans.append(A2-A1)
print(max(ans))
