#naming function follows the names as variables.

#name= "John" #I declared this attribute
def check_grade(marks, first_name, last_name):
    if marks <= 30:
        print(first_name+" "+last_name+" scored an F")
    elif marks > 30 and marks <= 40:
        print(first_name+" "+last_name+" scored an D")
    elif marks > 40 and marks <=50:
        print(first_name+" "+last_name+" scored an C")
    elif marks >50 and marks <= 60:
        print(first_name+" "+last_name+" scored an B")
    else:
        print(first_name+" "+last_name+" scored an A")

check_grade(56, "John", "Doe")
"""
import function
print(function.name)
"""