result = set()

for x in range(0, 10):
    for y in range(0, 10):
        num1 = int(f"73{x}1{y}6{x}")
        num2 = int(f"4{y}6{x}")
        result.add(num1 + num2)

print(len(result))
