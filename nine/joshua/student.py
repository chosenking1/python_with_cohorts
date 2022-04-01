# Author: Joshua
# Title :
class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    def set_name(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    def __repr__(self):
        return self.student_name, self.marks


studentone = Student("John", 19)
print(studentone.student_name, studentone.marks)
print(studentone.__repr__())

studentone.set_name("Otumba", 94)
print(studentone.student_name, studentone.marks)
print(studentone.__repr__())
