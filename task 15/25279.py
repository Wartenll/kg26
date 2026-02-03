
from itertools import combinations


def f(x):
    P = 66 <= x <= 67
    O = 32 <= x <= 1125
    T = 20 <= x <= 491
    A = A1 <= x <= A2
    return A <= (P or O or T)


line = [x for x in range(20, 1126) for eps in (0, 0.1, 0, 9)]
ans = []
for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(min(ans))