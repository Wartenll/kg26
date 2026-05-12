from re import finditer

with open(r'.././files/24_1975.txt') as file:
    data = file.readline()

# Паттерн для поиска последовательностей букв P
pattern = r'P[^P]*P'  # Например: от P до P, между ними нет других P

matches = [match.group() for match in finditer(pattern, data)]

if matches:
    longest = max(matches, key=len)
    print(len(longest))
else:
    print(0)


