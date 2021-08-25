def check_day(day_of_the_week):



    if day_of_the_week == "1" or day_of_the_week =="1.0":
        print("Monday")
    elif day_of_the_week == "2" or day_of_the_week =="2.0":
        print("Tuesday")
    elif day_of_the_week == "3" or day_of_the_week =="3.0":
        print("Tuesday")
    elif day_of_the_week == "4" or day_of_the_week =="4.0":
        print("Wednesday")
    elif day_of_the_week == "5" or day_of_the_week =="5.0":
        print("Thursday")
    elif day_of_the_week == "6" or day_of_the_week =="6.0":
        print("Thursday")
    elif day_of_the_week == "7" or day_of_the_week == "7.0":
        print("Friday")
    else:
       print('invalid value. enter a value that is an integer')

day_of_the_week = input("Enter an integer between 1 and 7: ")



check_day(day_of_the_week)

""" 
try:
    if int(day_of_the_week)==day_of_the_week:
        check_day(day_of_the_week)
    else:
        print("The value is not a valid integer")
except ValueError:#python problem
    print("Enter a valid integer")

        
try:
    (day_of_the_week) =int(input("Enter an integer between 1 and 7: "))
    check_day(day_of_the_week)
except ValueError:
    print("Enter a valid integer")

    day_of_the_week
    int(input("Enter a number between 1 and 7: "))
    check_day(day_of_the_week=)
    """