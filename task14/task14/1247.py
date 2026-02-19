n = 729**8 - 3**18 + 85
count = 0
while n > 0:
    if n % 9 == 0:
        count += 1
    n //= 9
print(count)