# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:18:05 2019

@author: Apple
"""
import turtle
myTurtle = turtle.Turtle()
myTurtle.pensize(10)
myTurtle.circle(50)
myTurtle.color("blue")
myTurtle.pensize(10)

myTurtle.penup()
myTurtle.setposition(-120, 0)
myTurtle.pendown()
myTurtle.circle(50)
myTurtle.color("green")
myTurtle.pensize(10)

myTurtle.penup()
myTurtle.setposition(60, 60)
myTurtle.pendown()
myTurtle.circle(50)
myTurtle.color("yellow")
myTurtle.pensize(10)

myTurtle.penup()
myTurtle.setposition(-60, 60)
myTurtle.pendown()
myTurtle.circle(50)
myTurtle.color("red")
myTurtle.pensize(10)

myTurtle.penup()
myTurtle.setposition(-180, 60)
myTurtle.pendown()
myTurtle.circle(50)
myTurtle.color("black")
myTurtle.pensize(10)

turtle.done()
