# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a=float(input("enter angle 1: "))
b=float(input("enter angle 2: "))
c=float(input("enter angle 3: "))

if(a==b==c):
    print("Triangle is equilateral")
elif(a==b or a==c or b==c):
    print("Triangle is isosceles")
else:
    print("Triangle is scelene")