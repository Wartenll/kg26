def f(x, y):
    return (x * y > A) and (x > y) or (11 > x)


for A in range(1000, -1000, -1):
    if all(f(x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break
