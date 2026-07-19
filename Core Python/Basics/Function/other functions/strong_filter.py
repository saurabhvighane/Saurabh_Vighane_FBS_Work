# write a program to filter strong no between 1 to 1000

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact


data = list(range(1,10000001))


res=list(filter(lambda n  : sum(fact(int(d)) for d in str(n)) == n  ,data ))

print(res)

# 145 = 1!+4+5

# n=145
# t=n
# sum=0
# while(t>0):
#     fact=1
#     d=t%10
#     t//=10
#     j=1
#     while(j<=d):
#         fact=fact*j
#         j+=1
#     sum+=fact
# if sum==n:
#     print("No is strong")

