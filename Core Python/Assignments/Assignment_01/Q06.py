# Write a Program to input two angles from user and find third angle of the triangle.

# Take input from user
Angle_1=float(input("Entet value of first angle : "))
Angle_2=float(input("Entet value of second angle : "))

# Perform operation
Angle_3= 180 - (Angle_1+Angle_2)

#Display result
print("Value of third angle of triangle is : ",Angle_3)