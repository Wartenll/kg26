ans = ['АЕКНС']
alph = 'СЕНЕКА'
word = {'А': 0, 'Е': 1, 'К': 2, 'Н': 3, 'С': 4}

result = 0
for letter in alph:
    result = result * 5 + word[letter]

print(result + 1)