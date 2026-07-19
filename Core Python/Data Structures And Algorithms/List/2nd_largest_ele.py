def Slargest(List):
    Max=li[0]
    Smax=li[0]
    for i in range(len(li)):
        if li[i]>Max:
            Smax=Max
            Max=li[i]
    return Max,Smax

def Clist(li):
    n=int(input("Enter how many no you want to add to list:"))
    for i in range(n):
        ele=int(input("Enter element:"))
        li.append(ele)
    return li

# li1=[10,20,30,40,50,40,70,10,90,100,110]
li=[]
List=Clist(li)
Max,Smax = Slargest(List)
print("Largest No:",Max)
print("Second Largest No:",Smax)
print("Max No using built in function:",max(li))    # using built in function

