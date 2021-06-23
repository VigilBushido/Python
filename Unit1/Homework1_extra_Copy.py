#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 02:41:43 2017

@author: sergiomac
"""

    
class Student(object):
    count = 0
    """A student with a name and date of birth
    
    Attributes:  
        name: (holds student name)
        age: (holds student age)
        birthmonth: (hold students birthmonth)
    """
    def __init__(self, name, age, birth_month):
        self.name = name
        self.age = age
        self.birth_month = birth_month
        Student.count += 1
        
    def displayName(self):
        "Returns students name is *name*"
        return self.name;
        
    def displayBirthmonth(self):
        "Returns students birth month"
#        import time
#        ## dd/mm/yyyy format
#        print (time.strftime("%d/%m/%Y"))
        return self.birth_month;

def main():
#        Student1 = Student(input("Enter a students name: "),input("Enter a students age: ")\
#                          ,input("Enter a students birth month: "))
        Student1 = Student('Sergio Munguia', 24, 'March')
        Student2 = Student('Omar Sawarez', 21, 'July')
        Student3 = Student('John Newman', 23, 'November')
#        Student2 = Student(input("Enter a students name: "),input("Enter a students age: ")\
#                          ,input("Enter a students birth month: "))
#        Student3 = Student(input("Enter a students name: "),input("Enter a students age: ")\
#                          ,input("Enter a students birth month: "))
        print("\n")
        print(Student1.displayName())
        print(Student2.displayBirthmonth())
        print("Total Student count: %d" % Student.count)

main()
