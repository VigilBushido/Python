#
#   Sergio Munguia
#
#   finalGrade.l.py
#   using loop statement
#
def main():

    total = 0
    print("Welcome to the COP1234 grade caclulator!")
    for i in range(3):
            print("\t Pleast enter student id" ,end=': ',)
            studentid = eval(input())
            print("\t Please enter your name",end=': ',)
            Name = input()
            print("\t Please enter your midterm and final grades (seperated by coma)",end =': ',)
            midterm, final = eval(input())
            print("\t Please enter your project grade",end =': ',)
            project = eval(input())
            final = (midterm + final + project)/3
            total = final + total
            print("\t Your average grade is", final,"")
            print()
            
    avgtotal = total/3
    print("The Class average is : ", avgtotal,"")

main()
    

    

    
    

