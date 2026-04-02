with open(r'.\files\9832.txt') as f:
    data = [list(map(int, i.split())) for i in f]

k = 0
for line in data:
    cnt = [line.count(x) for x in set(line)]
    if sorted(cnt) == [1, 1, 1, 2, 2]:
        rep = [x for x in set(line) if line.count(x) == 2]
        uniq = [x for x in set(line) if line.count(x) == 1]
        if sum(rep) > sum(uniq):
            k += 1

print(k)