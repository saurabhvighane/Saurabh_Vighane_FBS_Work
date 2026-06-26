# WAP to print all even numbers until n.

n=int(input("Enter no upto you want even no: "))
# i=1
# while(i<=n):
#     if(i%2==0):
#         print(i)
#     i+=1
for i in range(2,n,2):
    print(i)