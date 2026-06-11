# Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100)

p=int(input('enter amount:'))
r=int(input('enter rate(%):'))
t=int(input('enter time: '))

si=p*r*t/100

print('simple interest is: ',si)