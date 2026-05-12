n = 283**382 + 9**15 + 2**3
digits = []
while n:
    digits.append(n % 14)
    n //= 14
print(abs(digits.count(11) - digits.count(12)))