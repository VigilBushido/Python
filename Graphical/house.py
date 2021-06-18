#
#   Sergio Munguia
#
#   house.py
#
#   Build a house with five mouse clicks
#

import graphics
from graphics import * 

def main():
    # Draw the underlying window
    win = GraphWin("Design a House", 500,500)
    win.setCoords(0, 0, 100, 100)
    msg = Text(Point(50,90), "")
    msg.draw(win)

    # Draw the frame of the house
    msg.setText("Click on the lower left corner of the house")
    p1 = win.getMouse()
    p1.draw(win)
    msg.setText("Click on the upper right corner of the house")
    p2 = win.getMouse()
    p1.undraw()
    house = Rectangle(p1, p2)
    house.setFill("cyan")
    house.draw(win)

    # Draw the house door
    msg.setText("Click on the center of the top edge of the door")
    doorWidth = (p2.getX() - p1.getX()) / 5
    halfWidth = doorWidth / 2
    
    
    p3 = win.getMouse()
    p31 = p3.clone()
    p31.move(-halfWidth, 0)
    p32 = p3.clone()
    
    doorHeight = p3.getY() - p1.getY()
    p32.move(halfWidth, -doorHeight)
    door = Rectangle(p31, p32)
    door.setFill("black")
    door.draw(win)

    # Draw the house window
    msg.setText("Click on the center of the window")
    windowWidth = doorWidth / 2
    halfWWidth = windowWidth / 2
    
    p4 = win.getMouse()
    p41 = p4.clone()
    p41.move(-halfWWidth, -halfWWidth)
    p42 = p4.clone()
    p42.move(halfWWidth, halfWWidth)
    window = Rectangle(p41, p42)
    window.setFill("yellow")
    window.draw(win)

    # Draw the Roof
    msg.setText("Click on the peak of the roof")
    p5 = win.getMouse()
    p51 = Point(p1.getX(), p2.getY())
    # p52 = p2.clone()

    roof = Polygon(p51, p5, p2)
    roof.setFill("red")
    roof.draw(win)

    msg.setText("Click anywhere to QUIT")

    win.getMouse()
    win.close()
    
main()
