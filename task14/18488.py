for x in range(1, 100):
    N = 7 ** 666 + 7 ** 333 + 49 ** x - 343
    s = ''
    while N > 0:
        s = str(N % 7) + s
        N //= 7
    if s.count('6') == 49:
        print(x)
        break
