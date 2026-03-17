def conv(x, q):
    res = ''
    while x:
        res += str(x % q)
        x //= q
    return res[::-1]

ans = []
for n in range(1, 1000):
    r = conv(n, 3)
    if n % 3 != 0:
        r = '1' + r + r[-3:]
    else:
        r += conv(sum(int(i) for i in r) * 8, 3)
    r = int(r, 3)
    ans += [(abs(1220 - r), r)]
print(min(ans))