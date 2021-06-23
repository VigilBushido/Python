#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sergio Munguia 

Programming Languages : Dr. Shihong Huang
Python Assignment 1

"""
#(1)
print("Hello World")
#(2)
age = 24
#(3)
print("Hello World, I'm ", age, " today.")
#(4)
print("hello world".upper())
#(5)
a = 3.14
#(6)
b = int(a)
#(7)
c = str(a)
#(8)
print(a, type(a), b, type(b), c, type(c))
#(9)
favorite_things_to_eat = ("pizza", "philly cheese-steak sandwich","chicken wings")
#(10)
classes = {'Programming Languages': 'Shihong Huang',\
        'Operating Systems': 'Tami Sorgente', 'Artificial Intelligence':'Oge Marques'\
        ,'Python Programming':'Ionut Cardai'}
#(11)
print(classes)
print(favorite_things_to_eat)
#(12)
whole = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29\
         ,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55\
         ,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81\
         ,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
#(13)
div2 = []
div3 = []
div4 = []
div5 = []
#(14)
for i in range(len(whole)):
    if whole[i] % 2 == 0:
        div2.append(whole[i])
        if whole[i] % 4 == 0:
            div4.append(whole[i])
    elif whole[i] % 3 == 0:
        div3.append(whole[i])
    elif whole[i] % 5 == 0:
        div5.append(whole[i])
#(15)        
print("div2: \n",div2)
print("div3: \n",div3)
print("div4: \n",div4)
print("div5: \n",div5)
print("whole: \n", whole)
#(16)
divOver5 = []
#(17)
for j in range(len(whole)):
    if whole[j] not in div2 and whole[j] not in div3 and whole[j] not in div4 and \
    whole[j] not in div5:
        divOver5.append(whole[j])
#(18)
print("divOver5: \n",divOver5)
#(19)
def exp3(x):
    x = int(x**3)
    exponent3 = "x^3 = " + str(x)
    return(exponent3);

print(exp3(3))
#(20) & (21)    
for keys, values in classes.items():
    print ("keys: {} \tvalues: {}".format(keys, values))

# Extra Credit Class 
class Student(object):
    count = 0    
#   Attributes:  
#       name: (holds student name)
#       age: (holds student age)
#       birthmonth: (hold students birthmonth)

    def __init__(self, name, age, birth_month):
        self.name = name
        self.age = age
        self.birth_month = birth_month
        Student.count += 1
        
    def displayName(self):
        #Returns students name is *name*
        return print(self.name);
        
    def displayBirthmonth(self):
        #Returns students birth month"
        return print(self.birth_month);

def main():
        Student1 = Student('Sergio Munguia', 24, 'March')
        Student2 = Student('Omar Sawarez', 21, 'July')
        Student3 = Student('John Newman', 23, 'November')

        print("\n")
        Student1.displayName()
        Student2.displayBirthmonth()
        print("Total Student count: %d" % Student.count)

main()

        
        


