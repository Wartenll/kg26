from itertools import combinations


def f(x):
    P = 52 <= x <= 105
    Q = 0 <= x <= 53
    A = A1 <= x <= A2
    return ((not P) and (not Q) and (not A)) <= ((x ** 2) > 303601)

line = [x + eps for x in range(0, 106) for eps in (0,0.1,0.9)]
line_A = [0, 52, 53, 105]
line_x = [1.5, 52.5, 54.5]
ans = []
for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)
print(min(ans))
