def f(num):
    cnt = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            cnt += i
            if i != num // i:
                cnt += num // i
    return cnt


for num in range(1000, 10000):
    s = f(num)
    if s % 100 == 23:
        print(num, s)
