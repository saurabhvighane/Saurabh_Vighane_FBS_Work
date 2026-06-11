# Write a program to enter P, T, R and calculate simple Interest.

# Take input from user
P=float(input("Enter actual amount(p) : "))
R=float(input("Enter rate(r%) : "))
T=float(input("Enter time(t) : "))

# Perform operation
S_I=P*R*T/100

#Display result
print("Simple Interest is : ",S_I)