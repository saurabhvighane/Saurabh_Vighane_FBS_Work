# Find the sum of three-digit number.

n=int(input('enter 3 digit no: '))

d1=n % 10
n=n // 10
d2=n % 10
n=n // 10
d3= n % 10
n=n // 10
s=d1 + d2 +d3
a=d1*100+d2*10+d3
print(a)
print(f'sum of 3 digits are {s}')


