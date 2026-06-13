# Write a program to accept distance in km and convert it into meters and centimeters both.

km=float(input('enter distance in km: '))

m=1000*km
cm=100*m

print(f'distance in m:{m} and cm is:{cm}')