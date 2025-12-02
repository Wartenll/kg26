def convert(num, sys):
    res = ''
    while num:
        res = res + str(num % sys)
        num //= sys
    return res[::-1]

for x in range(1, 2401):
    num = 7 * 9 ** 210 + 6 * 9 ** 110-x
print()
