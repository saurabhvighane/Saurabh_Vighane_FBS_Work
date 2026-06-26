# WAP to print sum of series upto n.

n=int(input("Enter no upto you want sum: "))
# i=0
# s=0
# while(i<=n):
#     s=s+i
#     i+=1
# print(s)
s=0
for i in range(0,n+1):
    s+=i
print(s)