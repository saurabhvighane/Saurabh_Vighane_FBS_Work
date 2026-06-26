# 5. WAP to print Fibonacci series upto n.

n=int(input("Ente no upto you want to find fabonacci series: "))
i=1
a=-1
b=1
while(i<n):
    c=a+b
    print(c)
    a=b
    b=c
    i+=1