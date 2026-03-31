with open(r'.\filess\17_18176.txt') as file:
    data = [int(i) for i in file]
min_val = min(x for x in data if x > 0 and x % 10 == 4)
def sum_digits(n):
    return sum(int(d) for d in str(abs(n)))
ans = []
for i in range(len(data) - 2):
    s = sum_digits(data[i]) + sum_digits(data[i + 1]) + sum_digits(data[i + 2])
    if s == min_val:
        ans.append(data[i] + data[i + 1] + data[i + 2])
print(len(ans), max(ans))