from itertools import

# product - функция, которая формирует все возможные комбинации символов длинной repeat
alph ='poland'
for val in product(alph, repeat=3):
    val=''.join(val)

# permutations - функция, которая формирует
# все возможные перестановки
for val in permutations (alph):
    print(val)
# enumerate- нумерует элементы последовательности от start
res = enumerate(alph, start = 1)
print(*res)