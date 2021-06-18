#
#   Sergio Munguia
#
#   futval.py
#
#
import graphics
from graphics import *

def main():
    win = GraphWin("Investment Growth Chart", 300,400)
    win.setCoords(0, 0, 6, 8)

    Text(Point(3,7),"Plotting a 10 year investment").draw(win)
    msg = Text(Point(3,6),"Enter the information below")
    msg.draw(win)

    Text(Point(2,4), " Initial:").draw(win)
    Text(Point(2,3), " Initial rate:").draw(win)
    principal = Entry(Point(3,4), ).draw(win)
    principal.setText("0.0")
    principal.draw(win)
    principal = principal.getText()
    rate = Entry(Point(3,3), 5).draw(win)
    rate.setText("0.0")
    rate.draw(win)
    rate = rate.getText()
    
    interest = rate / 100

    newwin = GraphWin("Chart", 300,400)
    newwin.setCoords(0, 0, 10, 5)
    
    Text(Point(0,0),"0k").draw(newwin)
    Text(Point(0,1),"2.5k").draw(newwin)
    Text(Point(0,2),"5k").draw(newwin)
    Text(Point(0,3),"7.5k").draw(newwin)
    Text(Point(0,4),"10k").draw(newwin)
    Text(Point(0,0),"10k + ").draw(newwin)

    for i in range(1,11):
        principal = principal * (1 + interest)
        principalbar = principal
        greenbar = Rectangle(i, principalbar)
        greenbar.setFill("green")
        greenbar.setWidth(2)
        greenbar.draw(newwin)


    intrutxt.setText("Click anywhere to QUIT")

    win.getMouse()
    win.close()
    newwin.getMouse()
    newwin.close()

main()

    

    
    
