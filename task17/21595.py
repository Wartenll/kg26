with open(r'.\filess\17_21595.txt') as file:
    data = [int(i) for i in file]

k = sum(1 for x in data if 1000 <= abs(x) <= 9999 and abs(x) % 10 == 3)
k2 = k * k

ans = []
for i in range(len(data) - 2):
    a, b, c = data[i], data[i + 1], data[i + 2]
    if a + b + c - min(a, b, c) > k2:
        ans.append(a + b + c)

print(len(ans), abs(max(ans)))
