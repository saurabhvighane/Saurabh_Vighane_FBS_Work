# WAP to check if given number is Perfect Number.
# 6=1+2+3(divider)
n=int(input("Enter no to check no is perfect or not: "))
t=n

i=1
c=0
while(i<t):
    if t%i==0:
        c+=i
    i+=1
if c==n:
    print("No is perfect")
else:
    print("No is not perfect")
