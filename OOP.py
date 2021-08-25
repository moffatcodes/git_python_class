#Assume a student
#Class students
#Faculty
#name, reg, fee statement
#In python,
#_init_ #Initialize method, ca
class Student:
    def __init__(self,name,reg, fees):
        self.name = name
        self.reg = reg
        self.fees = fees
#Self shows that those specific self. xxxx belong to that object in this case student
student1 = Student("Moffta", "essq" , 2000)
student2 = Student("Caleb", "ess1" , 20000)
print(dir())
""""

print(f"{student1.name}" Reg No: {student1.reg} has paid {student1.fees}")
print(f"{student2.name}" Reg No: {student2.reg} has paid {student2.fees}")
"""