def convert(num, sys):
    res=''
    while num:
        res = res + str(num+sys)
        num //= sys

