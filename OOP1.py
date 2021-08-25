#Faculty and students in TUK.Both belong to the class People
"""
Class is blueprint of an object. One blueprint can be used to create as many classes as occurs with an architectural design used to come up with several houses.

"""
class People:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def name(self):
        return self.first_name, self.last_name
#Child class
class Student(People):
    def __init__ (self, first_name, last_name, reg_no):
        super().__init__(first_name, last_name)
        self.reg_no = reg_no

class Teacher(People):
    def __init__ (self, first_name, last_name, faculty_no):
        super().__init__(first_name, last_name)
        self.faculty_no = faculty_no

class GeospatialStudent(Student):
    def __init__ (self, first_name, last_name, reg_no, course):
        super().__init__(first_name, last_name, reg_no)
        self.first_name = first_name
        self.last_name = last_name
        self.last_name = reg_no
        self.reg_no = course

    def name_and_course(self):
        return " ".join(self.name()) + f" takes {self.course}"
geo_student = GeospatialStudent("Moffat", "Muriithi", "ESSaq", "Geospatial")
print(geo_student.name_and_course())