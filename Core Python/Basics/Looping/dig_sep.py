n=int(input("Enter no: "))
temp=n
c=0
while(temp>0):    # we use while loop when execution count is unpredictable
    d=temp%10
    temp//=10
    print(d)
    print(temp)
