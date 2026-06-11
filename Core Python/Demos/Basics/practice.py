# # Take an integer and convert it to float and string

# a=int((input("enter a no: ")))
# b=type(float(a))
# c=type(str(a))
# print(f' type of input value is:{a} conversions are: {b},{c}')


# # check data type

# a=5
# b=2.4
# f='st'
# print(a,b,f,type(a))


# swap

x=12
y=44
# print('before swap',x,y)

# # using third variable
# z=x
# x=y
# y=z
# print('after swap',x,y)

# without third variable
print('before swap',x,y)
x=x+y   #56=12+44
y=x-y    # 12=56-44
x=x-y    # 44=56-12
# print('before swap',x,y)


# average
a,b,c,d,e=77,54,77,33,99
print(a,b,c,d,e)
A=(a+b+c+d+e)/500 *100
print(A)

# greater no
a=8
b=32
c=((a>b)==True)
d=((a<b)==True)
print(c,d)
print('greater no is:',a if a>b else b)