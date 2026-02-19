from itertools import product

cnt = 0  # Счетчик (было c, но потом используется cnt)

for val in product('НЧЬЯ', repeat=7):
    val = ''.join(val)

    # Заменяем И и Я на *
    for i in 'ИЯ':
        val = val.replace(i, '*')

    # Проверяем условия
    if val.count('*') == 2 and '**' not in val:
        cnt += 1

print(cnt)