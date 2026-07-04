# print

#        *
#       * *
#      *   *
#     *     *
#    *       *
#     *     *
#      *   *
#       * *
#        *

for i in range(1,6):
    for j in range(6-i):
        print(" ",end="")
    for j in range(2*i-1):
        if j==0 or j==2*i-2:
            print("*",end=" ")
        else:
            print(" ",end="")
    print()    
for i in range(6-1,0,-1):
    for j in range(6-i):
        print(" ",end="")
    for j in range(2*i-1):
        if j==0 or j==2*i-2:
            print("*",end=" ")
        else:
            print(" ",end="")
    print()    