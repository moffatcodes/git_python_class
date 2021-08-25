"""
Write a program that awards users points according to the input the program receives
1. The program  should award points and print that the user gets.
- If the user's number is within one value of the right number, the user get 20 points
-If the user is within two values of the right number, the user get 10 points
-If the user's number is the right one, the user gets 1000 points.
-Use python functions
-functions, passing arguments in functions, data types, type conversion
to get the absolute value, write abs -4 =4
"""
"""
#To generate random values use, random.randint(0,10).This will generate values from 0 to 10
import random
#random.randint(10,20)
#python solves a problem step by step.
import random
users_input =int(input("Enter a number between 0 and 10: "))

def game():

    if users_input >10 or users_input<0:
        print("The user should enter value that is b2n 1 and 10")
    else:
        right_number = random.randint(0,10)
        if abs(right_number-users_input)==1:
            print("You have won 20 points:The correct is ", right_number)
        elif right_number ==users_input:
            print("You have won 10 points: The correct is ", right_number)
        elif abs(right_number-users_input)==2:
            print("You have won 1000 points")
        else:
            print("The user has not won any point:The correct is ", right_number)
game()
"""