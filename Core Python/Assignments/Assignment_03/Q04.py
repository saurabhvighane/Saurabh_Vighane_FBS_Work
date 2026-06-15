# Write a program to input all sides of a triangle and check whether triangle is valid or not.

a=float(input("enter angle 1: "))
b=float(input("enter angle 2: "))
c=float(input("enter angle 3: "))

if(a+b>c and b+c>a and a+c>b):
    print("Triangle is valid")
else:
    print("Triangle is invalid")