# Write a program to check if given 3 digit number is a palindrome or not.

a=int(input("Enter 3 digit no: "))

d1=a%10
a=a//10
d2=a%10
a=a//10
d3=a%10
a=a//10

sum=d1*100+d2*10+d3
rev=d3*100+d2*10+d1

if(sum==rev):
    print("No is palindrome")
else:
    print("No is not palindrome")