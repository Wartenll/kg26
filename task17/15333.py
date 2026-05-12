with open(r'.\filess\17_15333.txt') as file:
    data = [int(i) for i in file]
max_19 = max(x for x in data if x % 19 == 0)
ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i], data[i + 1]
    if num1 > max_19 or num2 > max_19:
        ans.append(num1 + num2)
print(len(ans), max(ans))