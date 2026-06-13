# Write a program to enter P, T, R and calculate Compound Interest.

# Take input from user
P=float(input("Enter actual amount(p) : "))
R=float(input("Enter rate(r%) : "))
T=float(input("Enter time(t) : "))

# Perform operation
C_I=P * (1 +(R /100)) **T - P

#Display result
print("Compound Interest is : ",C_I)
