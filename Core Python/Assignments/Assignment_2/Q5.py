# WAP to calculate selling price of book based on cost price and discount.

cost=(int(input('enter cost price of book')))
discount=int(input('enter discount(%)'))

disc=(cost*discount)/100 
sp=cost-disc

print('selling price is:',sp)