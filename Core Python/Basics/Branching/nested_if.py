g=input('enter gentder(m/f)')

a=int(input('enter age'))

if(g=='f'):
    if(a>=18):
        print('girl is eligible for marriage')
    else:
        print('girl is not eligible for marriage')
else:
    if(a>=21):
        print('boy is eligible for marriage')
    else:
       print('boy is not eligible for marriage')