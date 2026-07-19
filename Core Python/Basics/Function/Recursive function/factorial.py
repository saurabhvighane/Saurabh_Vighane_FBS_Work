# write a program to calculate a factorial using recursive function

def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)

n=5
res=factorial(n)
print(res)



def dig(n):
    if n>0:
        d=n%10
        print(d)
        n//=10
        dig(n)
n=121
dig(n)