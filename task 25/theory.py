from fnmatch import fnmatch
print(fnmatch('','*'))
# Задачи с масками

# Библиотека для проверки строк под маску
from fnmatch import fnmatch

# ? - ровно один любой символ
# * - любое кол-во любых символов

print(fnmatch('', '*'))


# КомпЕГЭ 4603 (рекомендованное решение)
from fnmatch import fnmatch

for N in range(12347 - 12347 % 141, 10 ** 8 + 1, 141):
   if fnmatch(str(N), '1234*7'):
       print(N, N // 141)

#########################################
print('#################')

# КомпЕГЭ 4603 (решение перебором)
from itertools import product

for l in range(0, 4):
    for val in product('0123456789', repeat=l):
        val = '1234' + ''.join(val) + '7'
        if int(val) % 141 == 0:
            print(val, int(val) // 141)


# Проверка на простоту
def if_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True
###################################################################
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