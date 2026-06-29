n=int(input("Enter no: "))
t=n
i=0
a=0
while(t>0):
    d=t%10
    t//=10
    i+=1
print(i)
t=n
while(t>0):
    d=t%10
    t//=10
    a+=d**i
print(a)
if(n==a):
    print("No is armstrong")
else:
    print("No is not armstrong")