# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

g=input('enter gentder(m/f): ')

a=int(input('enter age: '))

if(g=='f'):
    if(a>=18):
        print('girl is eligible for marriage')
    else:
        print('girl is not eligible for marriage')
if(g=='m'):
    if(a>=21):
        print('boy is eligible for marriage')
    else:
       print('boy is not eligible for marriage')
else:
    print("Enter valid gender (m/f)")