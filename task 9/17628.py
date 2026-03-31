with open(r'.\files\17628.txt') as f:
    data = [list(map(int, i.split())) for i in f]
cnt = 0
for line in data:
    max_num = max(line)
    min_num = min(line)
    sum_ost = sum(line) - max_num - min_num
    if max_num + min_num <= sum_ost:
        cnt += 1
print(cnt)