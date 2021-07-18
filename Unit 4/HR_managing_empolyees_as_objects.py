#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sergio Munguia 

Problem 3 - HR Matters
"""

class Employee(object):
    __name=""
    __base_salary=0.0
    __phone_number=""
    count = 0

    def __init__(self, name, salary, phone):
        self.__name = name
        self.__base_salary = salary
        self.__phone_number = phone
        Employee.count += 1

#Mutator Methods
    def set_name(self, name):
        self.__name = name

    def set_base_salary(self, base_salary):
        self.__base_salary = base_salary

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

#Accessor Methods
    def get_name(self):
        return self.__name

    def get_total_salary(self):
        return self.__base_salary

    def get_phone_number(self):
        return self.__phone_number

    def __str__(self):
        return 'Employee (%s, %s, %f)' % (self.__name,self.__phone_number, self.__base_salary)
    
    def __repr__(self):
        return self.__str__()

class Engineer(Employee):
    
    def get_name(self):
        return self.__name

    def get_total_salary(self):
        return self.__base_salary

    def get_phone_number(self):
        return self.__phone_number

class Manager(Employee):
    __bonus=0

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_bonus(self):
        return self.__bonus

    def get_total_salary(self):
        return self.__bonus+Employee.get_total_salary()
  
class CEO(Manager):
    __stock=0

    def set_stock(self, stock):
        self.__stock = stock

    def get_stock(self):
        return self.__stock

    def get_total_salary(self):
        return self.__stock+Manager.get_total_salary()

def print_staff(employee_list):
    for x in employee_list:
        print(x)
  
employee1 = Employee("Josh Lipton",10000,"754-7777777")
employee2 = Manager("Sophia Morales",100000,"561-2977777")
employee3 = CEO("Sergio Munguia",1000000,"954-7777777")
employee4 = Engineer("Jacob Ladder",50400,"495-9999999")

employee_list = [employee1, employee2, employee3, employee4]
print_staff(employee_list)
