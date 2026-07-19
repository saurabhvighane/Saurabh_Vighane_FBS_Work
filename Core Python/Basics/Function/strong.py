def facto(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def isstrong(n):
    temp=n
    sum=0
    while(temp>0):
        d=temp%10
        temp//=10

        fact=facto(d)

        sum+=fact

        if sum==n:
            return True

n=int(input("Enter no: "))
strong=isstrong(n)
print(strong)
