# Write a program to calculate profit or loss.

cp=int(input("Enter cost price: "))
sp=int(input("Enter selling price: "))

d=sp-cp

if(d<0):
    print("Loss")
elif(d==0):
    print("No profit not Loss")
else:
    print("Profit")