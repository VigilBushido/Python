#
#   Hangman.py
#
#   input: letter
#
#   processing: 1. display the window with noose only
#               2. get a letter from user
#               3. if letter == any letter in word
#                   - display the letter if its ==
#                   elif letter != any letter in word
#                       draw a body piece on hangman
#               4. receive a correct response or incorrect response
#               5. fill the empty space with correct letter
#               6. loop
#
#   For each letter guessed incorrectly, you will display it in a Text object and draw a body part
#   There are 6 body parts: Head => Body => Left arm => Right arm => Left leg => Right leg
#
#   Play will continue until all blanks are filled or player is hanged.
#
#   At the end of game, un-draw the body parts and reset the word. allow the user to play 
#   as many times as he/she wishes

import random
import graphics
from graphics import *

def main():

    random.seed()
        
    win = GraphWin("Hangman", 500,600)
    win.setCoords(0,0,20,30)
    win.setBackground("brown")

    # Draw base, pole, & noose to hang man
    base = Rectangle(Point(2,2),Point(13,4))
    base.setFill("brown")
    base.draw(win)
    basepost = Rectangle(Point(3,4),Point(4,22))
    basepost.setFill("black")
    basepost.draw(win)
    hoist = Rectangle(Point(4,22),Point(8,22))
    hoist.setFill("black")
    hoist.draw(win)
    string = Rectangle(Point(8,22),Point(8,19))
    string.setFill("black")
    string.draw(win)

    # Text spots
    msgHead = Text(Point(10,28), "Welcome to Hangman!")
    msgHead.setFace('times roman')
    msgHead.setSize(20)
    msgHead.draw(win)
    msg = Text(Point(10,27), "To start choose a letter")
    msg.draw(win)
    Ltext = Text(Point(12,25), "Enter a letter \nclick to continue... (a-z):")
    Ltext.setSize(12)
    Ltext.draw(win)

    # wrong answers
    wrong = ["_","_","_","_","_","_","_","_","_","_","\n_","_","_","_","_"]
    innerbox = Rectangle(Point(15,6),Point(19,9))
    outerbox = Rectangle(Point(14.5,5.5),Point(19.5,9.5))
    innerbox.setFill("grey")
    outerbox.setFill("white")
    innerbox.draw(win)
    outerbox.draw(win)
    wrongAnswers = Text(Point(17,7), wrong)
    wrongAnswers.draw(win)


    # button
    button = Rectangle(Point(16,22),Point(18,24))
    button.setFill("green")
    button.draw(win)
    buttontxt = Text(Point(17,23),"ENTER")
    buttontxt.setStyle('bold')
    buttontxt.draw(win)
    
    # readlines() into a list & select word randomly 
    book = open("words.txt", 'r')
    wordlist = book.readlines()
    n = random.randrange(0,20)
    word = wordlist[n]
    word = word.strip()

    
    
    lword = len(word)   # = 7
    fillblanks = "_" * lword
    fillblanks = list(fillblanks)

    i = 0
    wrong = 0
    used = "_"
    used = list(used)
    cont = ""

    # Entry
    while wrong < 7 and cont != "q":
        # keys
        correct = ""

        lbox = Entry(Point(16,25), 2)
        lbox.setText("")
        lbox.draw(win)

        win.getMouse()
        letter = (lbox.getText().upper())
        letter = letter.strip()
        

        if letter in word:
            correct = correct + letter
            new = ""
            for i in range(len(word)):
                if letter == word[i]:
                    fillblanks[i] = word[i]
                    new = fillblanks
                    
        else:
            used.append(letter)
            usedcopy = used
                    
        if correct != letter:
            msgHead.setText("Sorry it is NOT in the word.")
            wrong = wrong + 1
            usedspaces = Text(Point(17,8), usedcopy)
            usedspaces.draw(win)
        else:
            Text(Point(14,22), new).draw(win)

        if (wrong == 1):
            head = Circle(Point(8,19), 1.5)
            head.setFill("white")
            head.draw(win)
        elif (wrong == 2):
            body = Rectangle(Point(7,12), Point(9,17.5))
            body.setFill("white")
            body.draw(win)
        elif (wrong == 3):
            rightleg = Line(Point(7,12), Point(5, 8))
            rightleg.draw(win)
        elif (wrong == 4):
            leftleg = Line(Point(9,12), Point(11, 8))
            leftleg.draw(win)
        elif (wrong == 5):
            rightarm = Line(Point(7,17.5), Point(5,14))
            rightarm.draw(win)
        elif (wrong == 6):
            leftarm = Line(Point(9,17.5), Point(11,14))
            leftarm.draw(win)

        
    msgHead.setText("GAME OVER, YOU HAVE BEEN HUNG")
    msg.setText("click to quit")
    win.getMouse()
    win.close()
        
    
main()
    
    

    
