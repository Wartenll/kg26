max_num = 0
for n in range(1, 41):
    if n % 2 == 1:
        if bin(n)[-4:] == '1011':
            max_num = n

print(max_num)
