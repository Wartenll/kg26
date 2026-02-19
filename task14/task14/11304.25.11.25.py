num= ["11x73", "94662x53x", "6x41", "31x77", "9x82xx181"]

for x in range(16):
    total = 0
    for num in num:
        s = num.replace('x', hex(x)[2:])
        total += int(s, 16)

    if total % 15 == 0:
        print(total // 15)
        break