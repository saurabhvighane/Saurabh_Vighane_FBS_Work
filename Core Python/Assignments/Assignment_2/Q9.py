# Write a program to swap two numbers without using third variable.

a=int(input('enter no 1: '))
b=int(input('enter no 2: '))

print('before swap',a,b)
a=a+b
b=a-b
a=a-b
print('after swap',a,b)

# 10
# 20
# a=10+20
# b=a-b
# a=a-b