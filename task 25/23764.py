import fnmatch

results = []
limit = 10**10
divisor = 1917

for num in range(divisor, limit + 1, divisor):
    num_str = str(num)
    if fnmatch.fnmatch(num_str, '3?12?14*5'):
        results.append((num, num // divisor))

results.sort(key=lambda x: x[0])

for num, quotient in results:
    print(f"{num} {quotient}")