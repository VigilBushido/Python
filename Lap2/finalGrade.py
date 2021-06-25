#
#   Sergio Munguia
#
#   finalGrade.py
#
#
def main():
    
    print("Welcome to the COP1234 grade caclulator!")
    studentid = eval(input("Please enter you student id: "))
    Name = input("Please enter your name: ")
    midterm, final = eval(input("Please enter your midterm and final grades (seperated by coma):"))
    project = eval(input("Please enter your project grade: "))
    finalgrade1 = (midterm + final + project)/3
    print("Your average grade is", finalgrade1,"")
    
    print()

    studentid2 = eval(input("Please enter you student id: "))
    Name2 = input("Please enter your name: ")
    midterm2, final2 = eval(input("Please enter your midterm and final grades (seperated by coma):"))
    project2 = eval(input("Please enter your project grade: "))
    finalgrade2 = (midterm2 + final2 + project2)/3
    print("Your average grade is", finalgrade2,"")
    print()

    studentid3 = eval(input("Please enter you student id: "))
    Name3 = input("Please enter your name: ")
    midterm3, final3 = eval(input("Please enter your midterm and final grades (seperated by coma):"))
    project3 = eval(input("Please enter your project grade: "))
    finalgrade3 = (midterm3 + final3 + project3)/3
    print("Your average grade is", finalgrade3,"")
    print()
    avgtotal = (finalgrade1 + finalgrade2 + finalgrade3)/3
    print("The Class average of",Name,',',Name2,', and',Name3,' is : ',avgtotal,"")

main()
    

    

    
    
