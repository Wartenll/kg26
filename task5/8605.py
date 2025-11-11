for N in range(1, 100000):
    r=f'{x:b}'
    if x % 5 ==0:
        r+=r[-3:]
    else:
        r=r+f'{(x%5)*5:b}'

