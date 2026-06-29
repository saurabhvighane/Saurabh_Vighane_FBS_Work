n=int(input("Enter no: "))
# for i in range(1,n):
#     for j in range(1,n-i):
#         print("",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

for i in range(1,n):
    for j in range(1,i+1):
        print("",end=" ")
    for j in range(1,n-i):
        print("* ",end=" ")
    print()