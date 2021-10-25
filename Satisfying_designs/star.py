import turtle
from turtle import *
color('red', 'yellow')
begin_fill()
turtle.speed(0)
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()