# Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

n=int(input("Enter no to find no is armstrong or not: "))
t=n
i=0
s=0
while(t>0):
    i+=1
    t//=10
print(i)
t=n
while(t>0):
    d=t%10
    t//=10
    s+=d**i
if s==n:
    print("No is armstrong")
else:
    print("No is not armstrong")