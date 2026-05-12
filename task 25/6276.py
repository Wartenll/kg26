from fnmatch import fnmatch

for N in range(1010101-1010101,10**10,2023):
    if fnmatch(str(N), '1?1?1?1*1'):
        print(N,N//2023)
