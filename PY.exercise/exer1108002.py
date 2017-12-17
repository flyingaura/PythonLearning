# -*- coding: utf-8 -*-

from turtle import *
import time,random

def DrawRuler(width,height):
    if(width <= 5 or height <= 5):
        return

    forward(width)
    left(90)
    forward(height)
    backward(height)
    right(90)
    forward(width)
    backward(width)
    # left(180)
    DrawRuler(width // 2, height // 2)
    backward(width)
    DrawRuler(width // 2, height // 2)
    # backward()
    return

def RandomTurTle():
    Distance = 0
    # while(abs(pos()[0]) < 300 and abs(pos()[1]) < 300):
    while(Distance <= 1000):
        speed(1)
        colormode(255)
        pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pensize(random.randint(1,10))
        left(random.randint(0,360))
        APace = random.randint(10,200)
        if(APace >= 120):
            print('Now jumping ！')
            stamp()
            penup()
            goto(random.randint(-300,300),random.randint(-300,300))
        else:
            pendown()
            forward(APace)
            Distance += APace

    return Distance


reset()
# DrawRuler(100,120)
print(RandomTurTle())

print(pos())

# print(abs(pos()[0]) < 50)
done()