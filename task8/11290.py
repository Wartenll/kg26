cnt = 0
digits = '0123456789ABCDEF'

for i in range(16 ** 4):
    val = f'{i:04X}'
    if val[0] == '0' or val.count('9') != 1:
        continue
    if all((int(val[j], 16) % 2) != (int(val[j + 1], 16) % 2) for j in range(3)):
        cnt += 1

print(cnt)
