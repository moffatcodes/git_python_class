name= "John" #I decalred this attribute


marks=int(input("Enter the marks"))
def check_passed_or_failed():
    if marks <40:
        print("The student has failed")
    else:
        print("The student has passed")

def check_grade():
    if marks <= 30:
        print("The student scored an F")
    elif marks> 30 and marks <= 40:
        print("The student scored an D")
    elif marks > 40 and marks <=50:
        print("The student sscored an C")
    elif marks >50 and marks <= 60:
        print("The student scored an B")
    else:
        print("The student scored an A")

check_grade()
check_passed_or_failed()