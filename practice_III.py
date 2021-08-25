"""
phone_type=input("What is the name of your phone")
if phone_type=="Xiaomi":
    print("My phone name is Xiaomi")
else:
    print("My phone type is not Xiaomi.It is " ,phone_type )
    """


def check_passed_or_failed():
    if marks >40:
        print('The student passed')
    else:
        print('The student failed')


marks=int(input("How many marks did the student score?"))

if marks<= 30:
    print("The student scored an F")
elif marks>30 and marks  <=40:
    print("The student scored a D")
elif marks>40 and marks  <=50:
    print("The student scored a C")
elif marks >50 and marks <=60:
    print("The student scored a B")
else:
    print("The student scored an A")

import concatente
print(concatente.first_name)
"""
def check_grade(marks, first_name, second_name):
    if marks <= 30:
        print("first_name"+" second_name"+"scored an F")
    elif marks >30 and marks <=40:
        print("first_name " +" second_name"+"scored a D")
    elif marks >50 and marks<=60:
        print("first_name " +" second_name"+"scored a C")
    elif marks >70 and marks <=80:
        print("first_name " +" second_name"+"scored a B")
    else:
        print("first_name " +" second_name"+"scored an A")
check_grade(67,"Doe", "Kibe")
"""
