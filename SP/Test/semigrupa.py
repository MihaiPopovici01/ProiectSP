from student import *
class Semigrupa:
    students = []
    def __init__(self, nume):
        self.nume = nume
    
    def add(self, student):
        self.students.append(student)
    
    def __str__(self):
        str = self.nume
        return str
