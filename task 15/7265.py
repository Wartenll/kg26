for A in range(1, 200):
    ok = True
    for x in range(1, 1000):
        f = ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 100)
        if not f:
            ok = False
            break
    if ok:
        print(A)
        break