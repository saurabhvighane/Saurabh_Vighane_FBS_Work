
#    1               1 
#    1 2           2 1 
#    1 2 3       3 2 1 
#    1 2 3 4 5 4 3 2 1 

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range(2 * (n - i) - 1):
        print(" ", end=" ")

    for j in range(i, 0, -1):
        if j != 5:
            print(j, end=" ")
    print()