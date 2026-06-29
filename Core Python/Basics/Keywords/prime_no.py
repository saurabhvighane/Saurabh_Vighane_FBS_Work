# n=int(input("Enter no to find prime no upto n: "))
# i=2
# for i in range(i,n+1):
#     f=0
#     for j in range(2,i):
#         if(i%j==0):
#             f=1
#             break
#     if f==0:
#         print(i)


# code to know no is prime or not

# n=int(input("Enter no to check no is prime or not: "))
# # flag=0
# if n<=1:
#     print("Mein wo nahi jo apko chahiye")
# else:
#     for i in range (2,n):
#         if n%i==0:
#             # flag=1
#             print("No is not prime")
#             break
#     # if flag==0:
#     #     print("No is prime")
#     # else:
#     #     print("No is not prime")
#     else:
#         print("No is prime")


# print prime no in given range
str=int(input("enter start: "))
end=int(input("enter end: "))

for i in range(str,end+1):
    if i > 1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
