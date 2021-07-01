#
#   Sergio Munguia
#
#   quiz.py
#
#   Input: Score of the quiz (0-5)
#
#   Processing: 1. Make a list of the grades & assign to variable
#               2. Eval the user input
#               3. Print the grade of the number (0-5) 
#
#   Output: Show the grade of the score



def main():
    # define the variable
    grades = ["F","F", "D", "C", "B",
              "A"]
    # eval the score of the quiz 
    n = eval(input("Please enter the score for the quiz (0-5): "))

    # display grade by indexing the correct letter
    print("The grade is", grades[n] + ".")

main()

