class Student:
    studentcount=0   # static variable
    @staticmethod
    def greet():
        print(f'Welcome to {Student.collageName}')

    def __init__(self,RollNo,Name,Marks):
        self.RollNo = RollNo
        self.Name = Name
        self.Marks = Marks
        Student.studentcount+=1

    def getId(self):
        return self.RollNo
    def setId(self,RollNo):
        self.RollNo = RollNo

    def getname(self):
        return self.Name
    def setname(self,Name):
        self.Name = Name

    def getMarks(self):
        return self.Marks
    def setMarks(self,Marks):
        self.Marks = Marks

    def display(self):
        print(f'RollNo={self.RollNo} \t Name={self.Name} \t Marks={self.Marks}')

class Placedstudent(Student):
    def __init__(self,RollNo,Name,Marks,sal):
        super().__init__(RollNo,Name,Marks)
        self.sal = sal
    def display(self):
        print(f'sal={self.sal}\t',end="")
        return super().display()
       


s1 = Student(101,'Sachin',90)
s2= Student(18,'Vrrat',88)
s3 = Placedstudent(45,'Rohit',99,45000)

# Student.greet()
s1.display()
s2.display()
s3.display()