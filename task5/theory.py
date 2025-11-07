# системы счисления
# двоичная система (binary)

N=25

print(bin(N)[2:])
print(f'{N:b}')
# bin() - переводит десятичное число в двоичную систему.
# Принимает на вход int, возвращает str.
# [2:] - срез, убирающий первые два символа '0b'
# f'' - форматируемая строка, которая позволяет вставлять в себя переменные
# восьмеричная система
print(oct(N)[2:])
print(f'{N:o}')

#16 system
print(hex(N)[2:])
print(f'{N:o}')
# Перевод в любую систему счисления (2 <= sys <= 9)
def convert(num, sys):
    res = ''
    # Пока целая часть не ноль, продолжаем делить
    while num != 0:
        # Получаем остаток, приписываем к результату
        res += str(num % sys)
        # Получаем новую целую часть
        num //= sys
    # Переворачиваем строку (записываем остатки в обратном порядке)
    return res[::-1]
# перевод в любую систему (2 <= sys <= 36
from string import printable as alph
def convert2(num, sys):
    res = ''
    while num != 0:
        res += alph[num % sys]
        num//= sys
    return res[::-1]


# перевод в 10 систему
num_bin ='101'
num_tri = '201'
num_hex = 'f01'
print(int(num_bin, 2))
print(int(num_tri, 3))
print(int(num_hex, 16))
