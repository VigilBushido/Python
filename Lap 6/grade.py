#
#   Sergio Munguia
#
#   grade.py
#
#   input: exam score
#
#   processing: using a multi  select the proper grade
#
#   
#
#

def main():

    print("Exam Grader")
    print()

    score = eval(input("Enter the score: "))

    if score >= 90:
        n = "A"
    elif 90 > score >= 80:
        n = "B"
    elif 80 > score >= 70:
        n = "C"
    elif 70 > score >= 60:
        n = "D"
    else:
        60 > score
        n = "F"

    print("The grade is " + n)

main()

    
