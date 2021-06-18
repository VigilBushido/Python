#
#   Sergio Munguia
#
#   target.py
#
#

import graphics
from graphics import *

def main():

    win = GraphWin("Archery Target", 400, 400)
    win.setCoords(-6,-6,6,6)
    win.setBackground('grey')

    circle5 = Circle(Point(0,0), 5)
    circle5.setFill('white')
    circle5.draw(win)
    circle4 = Circle(Point(0,0), 4)
    circle4.setFill('black')
    circle4.draw(win)
    circle3 = Circle(Point(0,0), 3)
    circle3.setFill('blue')
    circle3.draw(win)
    circle2 = Circle(Point(0,0), 2)
    circle2.setFill('red')
    circle2.draw(win)
    circle = Circle(Point(0,0), 1)
    circle.setFill('yellow')
    circle.draw(win)


    win.getMouse()
    win.close

main()
    
