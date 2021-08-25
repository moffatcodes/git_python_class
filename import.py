"""
import math #python standard library


print(math.sqrt(100))
"""
def check_grade(marks, first_name, second_name):
    if marks <= 30:
        print("The student scored an F")
    elif marks>30 and marks<=40:
        print("The student scored a D")
    elif marks >40 and marks <50:
        print("The student scored a C")
    elif marks >50 and marks <=60:
        print("The student scored a B")
    else:
        print("The student scored an A")

check_grade(23 ,"John","Doe")
