alph = 15 * (49**237) + 37 * (343**500) - 14 * (7**35)
cnt = []

while alph > 0:
    cnt.append(alph % 49)
    alph //= 49

count = sum(1 for d in cnt if d > 15)
print(count)