def F(N):
    if N < 3: return 1
    if N % 2 == 0: return F(N - 1) + N - 1
    return F(N - 2)+ 2 * N -2
print(F(34))
