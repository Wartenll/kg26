def f(x):
    B = 59 <= x <= 70
    return (x % A == 0) or ((x % 23 == 0) <= (not B))


for A in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break
