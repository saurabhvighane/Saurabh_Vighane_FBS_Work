# WAP to print factorial of a number .
n=int(input("Enter no to find factorial: "))
# i=n-1
# t=n
# while(i>0):
#     t=t*i
#     i-=1
# print(t)

t=1
for i in range(1,n+1):
    t=t*i
print(t)