
#  Модуль черепахи
from turtle import *
# изменение рахмер экрана
screensize(3000 , 3000)

# отключение аним
tracer(False)

# размер
m = 20

for i in range(2):
    fd(10 * m)
    rt(90)
    fd(18 * m)
    rt(90)


up()
fd(5 * m)
rt(90)
fd(7 * m)
lt(90)
down()

for i in range(2):
    fd(10 * m)
    rt(90)
    fd(7 * m)
    rt(90)

up()
for x in range(-10,25):
    for y in range (-25, 10):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()