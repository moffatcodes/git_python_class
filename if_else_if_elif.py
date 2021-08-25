#   if there are more than two conditions, then use elif
#The first condition is if, the second condition is else, if there is another cond.


marks =int(input("Enter the marks: "))

if marks <=30:
    print("The student scored an F")
elif marks >30 and marks <=40:
    print("The student scored a D")
elif marks >40 and marks <=50:
    print("The student scored a C")
elif marks >50 and marks <=60:
    print("The student scored a B")
else:
    print("The student scored an A")


