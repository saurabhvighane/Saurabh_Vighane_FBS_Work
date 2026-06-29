n=int(input("Enter no: "))
temp=n
c=0
while(temp>0):
    d=temp%10
    temp//=10
    c+=1
print(c)