# write program to find area and perimiter accept length breadth and radius
l=int(input('enter length:'))
b=int(input('enter breadth: '))
r=int(input('enter radius: '))


area=l*b+(0.5*3.14*r**2)
p=(2 * l) + b + 3.14*r 

print(f'area is: {area} and perimeter is: {p}')