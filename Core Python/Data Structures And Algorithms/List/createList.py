def createList(li):
    n=int(input("Enter how many elements you want to add:"))
    for i in range(n):
        ele=int(input("Enter element to add: "))
        li.append(ele)
    

li = []
createList(li)
print(li)