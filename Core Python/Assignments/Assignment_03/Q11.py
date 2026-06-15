# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

a1=int(input("Enter person 1 age: "))
a2=int(input("Enter person 2 age: "))
a3=int(input("Enter person 3 age: "))
a4=int(input("Enter person 4 age: "))
a5=int(input("Enter person 5 age: "))
amt=int(input("Enter ticket per person: "))

ct=70*amt/100
st=50*amt/100

if(a1<=12):
    t=ct
elif(a1>=59):
    t=st
else:
    t=amt

if(a2<=12):
    t+=ct
elif(a2>=59):
    t+=st
else:
    t+=amt


if(a3<=12):
    t+=ct
elif(a3>=59):
    t+=st
else:
    t+=amt


if(a4<=12):
    t+=ct
elif(a4>=59):
    t+=st
else:
    t+=amt


if(a5<=12):
    t+=ct
elif(a5>=59):
    t+=st
else:
    t+=amt

print("Total amount is: ",t)