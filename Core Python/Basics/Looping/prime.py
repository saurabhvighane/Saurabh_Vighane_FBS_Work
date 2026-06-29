
n=int(input("Enter no to find prime no upto that: "))
i=2
while(i<n):
    j=2
    f=0
    while(j<i):
        if(i%j==0):
            f=1
        j+=1
    if(f==0):  
        print(i)
    i+=1