# WAP to print all integers upto n that aren’t divisible by 2 and 3.

n=int(input("Enter no: "))
i=1
while(i<=n):
    if(i%2!=0 and i%3!=0):
        print(i)
    i += 1
   