# print

#            A 
#          A B C
#        A B C D E
#      A B C D E F G
#    A B C D E F G H I

for i in range(1,6):
    for j in range(5-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print(chr(65+j),end=" ")
    print()