# WAP to check if given number Strong Number.
# 145=1! +4! +5!
n=int(input("Enter no to find strong or not: "))
t=n
s=0
while(t>0):
    d=t%10
    t//=10
    f=1
    j=1
    while(j<=d):
        f=f*j
        j+=1
    s=s+f
if s==n:
    print("Strong no")
else:
    print("Not strong")

