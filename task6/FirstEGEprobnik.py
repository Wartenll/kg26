# Модуль turtle
from turtle import *

m=7

tracer(False)

forward (20 * m)
left(270)
fd(12 * m)
right(90)

forward (20 * m)
left(270)
fd(12 * m)
right(90)

up()

fd(9)
right(90)
fd(7)
left(90)

down()

fd(13 * m)
right(90)
fd(6 * m)
right(90)

fd(13 * m)
right(90)
fd(6 * m)
right(90)

up()

for x in range(-10, 25):
    for y in range(-25, 10):
        goto(x * m, y * m)
        dot(3, 'red')
update()
done()