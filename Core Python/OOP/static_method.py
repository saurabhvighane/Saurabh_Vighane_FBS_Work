class Student:

    collageName = 'FBS'
    @staticmethod
    def greet():
        print(f"Welcome to {Student.collageName}")
    def __init__(self,rn,name,marks):
        self.rn = rn
        self.name = name
        self.marks = marks

    def getrn(self):
        return self.rn   
    def setrn(self,rn):
        self.rn = rn 

    def getname(self):
        return self.name  
    def setname(self,name):
        self.name = name 

    def getmarks(self):
        return self.marks 
    def setmarks(self,marks):
        self.marks = marks 

    def display(self):
        print(f'Roll no:{self.rn} \t Name:{self.name} \t Marks:{self.marks} \t CollageName:{Student.collageName}')

Student.greet()
s1 = Student(45,'Rohit',90)
s1.setrn(11)
# print(s1.getrn())
s2 = Student(18,'Virat',85)
s1.display()
s2.display()
s2.setmarks(89)
s2.display()
# print(Student.collageName)
# print(s1.collageName)

