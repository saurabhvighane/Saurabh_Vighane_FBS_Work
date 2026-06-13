# Write a program to reverse three-digit number.

n=int(input('enter 3 digit no: '))

d1=n % 10
n=n // 10
d2=n % 10
n=n // 10
d3=n % 10
n=n // 10

rev=d1*100 + d2*10 +d3
print(f'sum of 3 digits are {rev}')


