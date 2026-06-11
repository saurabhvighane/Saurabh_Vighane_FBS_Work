# Write a program to calculate the percentage of student based on marks of any 5 subjects.

# Take input from user
m1=int(input("Enter marks for sub 1 : "))
m2=int(input("Enter marks for sub 2 : "))
m3=int(input("Enter marks for sub 3 : "))
m4=int(input("Enter marks for sub 4 : "))
m5=int(input("Enter marks for sub 5 : "))

# Perform operation
marks=m1+m2+m3+m4+m5
percentage=((marks/500)*100)

#Display result
print("total marks:",marks)
print("percentage of total marks is:",percentage,'%')