# WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

basic=int(input('enter basic salary: '))

da=(basic*10)/100
ta=basic*12/100
hra=basic*15/100

total_sal=basic+da+ta+hra
print('total salary: ',total_sal)
