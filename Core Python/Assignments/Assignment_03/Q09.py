# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
per = (total / 500) * 100

print("Total Marks =", total)
print("Percentage =", per)

if per >= 75:
    print("Grade: First class")
elif per >= 60:
    print("Grade: Second Class")
elif per >= 50:
    print("Grade: Third Class")
elif per >= 35:
    print("Grade: Pass Class")
else:
    print("Grade: Fail")
