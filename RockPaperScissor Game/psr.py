#
#   Sergio Munguia
#
#   rps.py
#
#   input: (1-3) or q to quit
#
#   processing: 1. ask the user from the menu to select an option
#                   a. See the rules
#                   b. play the game
#                   c. see the score results
#                   d. quit
#                   
#               2. while playing the game keep score
#               3. display the winner
#
#   output: show a menu & options to play the game, see the rules, or quit
#
#   project 2
#
#   


def menu():
    print("Rock, Paper, Scissors Menu")
    print("-"*20)
    print()
    print("1. See the rules")
    print("2. Play the game")
    print("3. Score")
    print("4. quit")
    print()
    x = eval(input("Please enter (1-4): "))
    if x == 1:
        rules()
    elif x == 2:
        main()
        scoreboard(player1, player2)
    elif x == 3:
        print()
    elif x == 4:
        quitg()
    else:
        print("ERROR! you entered incorrectly")
        print()
        menu()

def scoreboard(player1, player2):
    if player1 == 0 and player2 == 0:
        print("No Games Have Been Played")
    else:
        print("Player 1 has won,", player1)
        print("VS".center(20))
        print("Player 2 has won,", player2)
        i = input("Hit <enter> to return to menu")
        print()
        if i == "":
            menu()
    return player1, player2

def main():
    print("* Welcome to Rock , Paper , Scissors Game *")
    print("*"*43)
    print()

    x = "true"
    q = ""

    player1round, player2round = 0, 0
    player1points, player2points = 0, 0

    while x == "true":

        while player1points < 3 and player2points < 3:
                
            print("SCORE: Player 1 - ", player1points,"| Player 2 - ", player2points) 
            print()
            print("*Player 1* Menu to choose weapon")
            print("1.) Rock")
            print("2.) Paper")
            print("3.) Scissors")
            print("Player 1 enter in your weapon of choice: ")
            player1num = eval(input())

            print("*Player 2* Menu to choose weapon")
            print("1.) Rock")
            print("2.) Paper")
            print("3.) Scissors")
            print("Player 2 enter in your weapon of choice: ")
            player2num = eval(input()) 

            if player1num == q or player2num == q:
                print("Quitting Game ...")
                print()
                x = "false"
                menu()

            new1points, new2points = playerchoice(player1num, player2num)
            player1points = player1points + new1points
            player2points = player2points + new2points


        if player1points > player2points:
            print("Player 1 Has Won the Round!", player1points, ">", player2points)
            print()
            player1round = player1round + 1
            while player1round > 0:
                player1win = player1round + player1round
                menu()
            
        else:
            print("Player 2 Has Won the Round!", player2points, ">", player1points)
            print()
            player2round = player2round + 1
            while player2round > 0:
                player2win = player2round + player2round
                menu()

        scoreboard(player2win, player1win)        
        innumber1, innumber2 = scoreboard(player1, player2)
        
    
def playerchoice(player1num, player2num):

    player1num = int(player1num)
    player2num = int(player2num)
    print()
    player1points = 0
    player2points = 0

    if player2num == 1 and player1num == 3:
        print("Player2 wins: Rock beats Scissor!")
        player2points = player2points + 1
    elif player2num == 2 and player1num == 1:
        print("Player2 wins: Paper beats Rock!")
        player2points = player2points + 1
    elif player2num == 3 and player1num == 2:
        print("Player2 wins: Scissors beats Paper!")
        player2points = player2points + 1
    elif player2num == 1 and player1num == 2:
        print("Player1 wins: Paper beats Rock!")
        player1points = player1points + 1
    elif player2num == 2 and player1num == 3:
        print("Player1 wins: Scissors beats Paper!")
        player1points = player1points + 1
    elif player2num == 3 and player1num == 1:
        print("Player1 wins: Rock beats Scissors!")
        player1points = player1points + 1

    elif player2num == player1num:
        print("Draw")


    else:
        print("!!!???? Invalid input ????!!!")
        print()

    return player1points, player2points


def rules():
    print("*"*20)
    print("RULES".center(20))
    print("*"*20)
    print("-"*20)
    print("Paper covers Rock")
    print("Rock smashes Scissors")
    print("Scissors cut Paper")
    print()
    print("To quit the game, enter q as your choice")
    print("-"*20)
    print()
    i = input("Hit <enter> to return to menu")
    print()
    if i == "":
        menu()


def quitg():
    print("Thank you, Goodbye")

menu()
                  
            
    


    

    
    
