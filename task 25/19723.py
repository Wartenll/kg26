from fnmatch import fnmatch

for N in range(1004513 - 1004513 % 451 + 1,10**9 , 451):
    if fnmatch(str(N), '10?451*3'):
        print(N, N // 451)
