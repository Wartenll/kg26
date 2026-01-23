def convert(num, sys):
    res = ''
    while num:
        res = res + str(num % sys)
        num //= sys
    return res[::-1]
ans=[]
num = 5 * 343**2031 + 4 * 49**2142 - 3 * 7**111 + 7**222
R = convert(num,7)
ans = sum(map(int))
print(ans)