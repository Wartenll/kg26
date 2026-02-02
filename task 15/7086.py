def del_n(m, n): return m % n == 0
B = range(50, 71)
for A in range(1000, 0, -1):
    if all(del_n(x, A) or (not (x in B) or not del_n(x, 16)) for x in range(1, 1000)):
        print(A); break