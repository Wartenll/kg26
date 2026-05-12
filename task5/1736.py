ans = []

for N in range(1, 100000):
    binary_N = bin(N)[2:]
    new_binary = ''
    for digit in binary_N:
        if digit == '1':
            new_binary += '11'
        else:
            new_binary += '00'
    R = int(new_binary, 2)

    if R > 63:
        ans.append(R)

print(min(ans))