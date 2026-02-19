from string import printable as alph

for x in alph[:22]:
    num1 =int(f'18{x}38596', 23)
    num2 =int(f'80{x}33', 23)
    num3 =int(f'521{x}6', 23)
    num = num1 + num2 + num3
    if num % 22 == 0:
        print(x, num // 22)