num = 4 * 16 ** 36 + 3 * 16 ** 29 - 4 * 16 ** 19 + 4 * 16 ** 15 + 2 * 16 ** 7 - 4 * 16 ** 6 + 4 * 16 ** 3 + 9

digits = set()
while num > 0:
    digits.add(num % 16)
    num //= 16

print(len(digits))
