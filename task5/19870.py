def convert (num, sys):
    res = ''
    while num !=0:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'
ans = []

print(convert(0,4))