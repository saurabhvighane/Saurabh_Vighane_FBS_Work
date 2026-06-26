# WAP to check if a given number is prime number or not.
# no divided by 1 and itself only
n=int(input("Enter no to find prime or not: "))
flag=0
i=2
if n<1:
    print("Enter no above 1")
else:
    while(i<=n):
        if n%i==0:
            flag=1
            break
        i+=1
    if flag==0:
        print("No is prime")
    else:
        print("No is not prime")

