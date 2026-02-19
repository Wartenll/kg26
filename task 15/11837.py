def f(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not ((x*x + y*y > 1024 - x) or (y < -2*x + A)):
                return False
    return True

for A in range(1000, -1000, -1):
    if f(A):
        print(A)
        break