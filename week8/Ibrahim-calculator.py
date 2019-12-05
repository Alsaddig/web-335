#/*
#============================================
#; Title: Python in Action
#; File Name: thomason_calculator.py
#; Author: Alsaddig Ibrahim
#; Date:   04 December 2019
#; Description: Calculator Python
#;===========================================
#*/
first_name = "Alsaddig"

last_name = "Ibrahim"
date="december /04 /2019"

print('Name: '+first_name + ' ' + last_name)
print('Date: '+date)
print("__________________________________________")
def add(param1, param2):
    return param1 + param2

def subtract(param1, param2):
    return param1 - param2

def divide(param1, param2):
    return param1 / param2
    
print(add(4, 6))
print(subtract(9, 3))
print(divide(50, 10))