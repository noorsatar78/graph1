

import turtle
import random
import time

 
def triangle(points,color,sakwe):
    sakwe.fillcolor(color)
    sakwe.up()
    sakwe.goto(points[0][0],points[0][1])
    sakwe.down()
    sakwe.begin_fill()
    sakwe.goto(points[1][0],points[1][1])
    sakwe.goto(points[2][0],points[2][1])
    sakwe.goto(points[0][0],points[0][1])
    sakwe.end_fill()

# TO GET THE MID POINTS ON THE THREE SIDES OF THE TRIANGLE

def midPoint(ps1,ps2):

    return ( (ps1[0]+ps2[0]) / 2, (ps1[1] + ps2[1]) / 2)

# Defining the function for the whole structure

''' FOR EVERY ONE TRIANGLE, a degree -1 takes it to the other one which is linked to
 the wall and begins the process all over '''


def triangleFull(points,degree,sakwe):

    colorGroup = ['green','white','white','white'] # color for the four shapes
    triangle(points,colorGroup[degree],sakwe)


    if degree > 0: # This part produces all the internal smaller triangles
        triangleFull([points[0],
                        midPoint(points[0], points[1]),
                        midPoint(points[0], points[2])],
                   degree-1, sakwe)
        triangleFull([points[1],
                        midPoint(points[0], points[1]),
                        midPoint(points[1], points[2])],
                   degree-1, sakwe)
        triangleFull([points[2],
                        midPoint(points[2], points[1]),
                        midPoint(points[0], points[2])],
                   degree-1, sakwe)

def main():
   sakwe = turtle.Turtle()
   GUI = turtle.Screen()
   myPoints = [[-200,-100],[0,200],[200,-100]]
   triangleFull(myPoints,3,sakwe)
   GUI.exitonclick()

main()
