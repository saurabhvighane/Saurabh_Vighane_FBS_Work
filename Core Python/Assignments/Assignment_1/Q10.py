# Write a program to calculate area of an equilateral triangle.

# Take input from user
side=float(input("Enter the side of triangle : "))

# Perform operation
area = ((3 ** 0.5)/4) * (side ** 2)   #underroot 3/4 side^2

#Display result
print("Area of equilateral triangle is : ",area)