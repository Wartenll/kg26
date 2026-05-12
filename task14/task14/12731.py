for x in range(0, 14):
    n1 = int('9' + str(x) + 'AB', 13)
    n2 = int(str(x) + '46C', 16)
    n3 = int('B7' + str(x), 15)
    total = n1 + n2 - n3
    if total % 14 == 0:
        print(total // 14)
        break