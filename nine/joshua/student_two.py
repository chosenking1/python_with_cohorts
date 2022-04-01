# Author: Joshua
# Title :

class SecondStudentMethod:
    def __init__(self, student_id):
        self.student_id = student_id
        self.student_name = "student_name"
        self.score = 0

    def set_student_id(self, student_id, name):
        self.student_id = student_id
        self.student_name = name

    def set_student_score(self, name):
        self.score = name

    def __repr__(self):
        return self.student_id, self.student_name, self.score

    def two__repr__(self):
        return self.student_id, self.score


student_one = SecondStudentMethod(1234, )
print(student_one.__repr__())

student_one.set_student_id(1234, "Majeck")
student_one.set_student_score(100)
print(student_one.two__repr__())
