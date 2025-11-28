def convert (num, sys):
    res = ''
    while num !=0:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for N in range(1, 100_000):
    R = convert(N, 4)
    if sum(map(int, R)) % 3 == 0:
        R = R.replace('0', '*' )
        R = R.replace('2', '0')
        R = R.replace('2', '2')
    else:
        R=R[0]+'10'+R[3:] + '33'
    R = int(R,4)
    if R > 320:
        ans.append([R,N])

min_R=min(ans)[0]
ans_2 =[]
for i in ans:
    if i[0] == min_R:
        ans_2.append(i[1])
    print(max(ans_2))


