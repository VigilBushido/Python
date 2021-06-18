#
#
#   Sergio Munguia
#
#   graphicsTest.py
#
#   Test the graphics library classes  & Objects 
#       

# Import Graphics library

import graphics 
from graphics import *

def main():
    # Create a window titled Shapes with a size of 500x500 pixels
    win = GraphWin("Shapes", 500, 500)

    # Create & Draw a red circle, located at 100x100 with a radius of 50
    circle = Circle(Point(100,100), 50)
    circle.setFill("red")
    circle.setOutline("red")
    circle.draw(win)

    circle2 = circle.clone()
    circle2.move(300,0)
    circle2.draw(win)

    # Create & Draw a blue two-way arrow
    line = Line(Point(100,250), Point(400, 250))
    line.setFill("blue")
    line.setArrow("both")
    line.draw(win)

    # Create & Draw a green ectangle
    rectangle = Rectangle(Point(100,300), Point(400,400))
    rectangle.setFill("green")
    rectangle.setOutline("yellow")
    rectangle.draw(win)

    # Creat & Draw a text object
    message = Text(Point(250,450), "Shapes in Python are Fun!")
    message.setStyle("bold italic")
    message.setTextColor("cyan")
    message.draw(win)

    win.getMouse()
    win.close()

main()
