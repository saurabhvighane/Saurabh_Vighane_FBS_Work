# 3. Create object of student class (Outside SY & TY package) having roll
# number, name, SYMakrs and TYMarks. Add the marksof SY and TY
# Computer subjects and calculate grade ("A" for >=70, "B" for >=60,
# "C" for >=50, “Pass Class” for >=40 else “Fail”) and display the result
# of the student in proper format.

from SY.symarks import SYMARKS
from TY.tymarks import TYMARKS

class Student:
    def __init__(self,roll_no,name,sy_marks,ty_marks):
        self.roll_no=roll_no
        self.name=name
        self.sy_marks=sy_marks
        self.ty_marks=ty_marks

    def calculate_result(self):
        total=(self.sy_marks.computer_total+
        self.ty_marks.theory+
        self.ty_marks.practical)

        if total>=70:
            grade='A'
        elif total >= 60:
            grade = "B"
        elif total >= 50:
            grade = "C"
        elif total >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"
        
        return total,grade

    def display(self):

            total, grade = self.calculate_result()

            print("\n----- Student Result -----")
            print(f"Roll No: {self.roll_no}")
            print(f"Name: {self.name}")
            print(f"SY Computer Marks: {self.sy_marks.computer_total}")
            print(f"TY Theory Marks: {self.ty_marks.theory}")
            print(f"TY Practical Marks: {self.ty_marks.practical}")
            print(f"Total: {total}")
            print(f"Grade: {grade}")


sy=SYMARKS(88,90,99)
ty=TYMARKS(77,88)

student1=Student(1,'saurabh',sy,ty)
student1.display()


