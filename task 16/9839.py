from sys import setrecursionlimit

def f(N):
    if N < 3: return 3
    return 2 * N + 5 + f(N - 2)
setrecursionlimit(1600)
print(f(3027)-f(3023))
############################################
