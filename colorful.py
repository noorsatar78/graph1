# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:34:29 2019

@author: Apple
"""

import turtle
t=turtle.Turtle()
colors=['green','red','purple','blue','orange']
t.pensize(1)
t.speed(300)
for x in range(200):
    t.pencolor(colors[x % 5])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
turtle.done()