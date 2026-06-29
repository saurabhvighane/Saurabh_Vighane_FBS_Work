import random


user=input("enter username: ")
p=input("enter password: ")

username="admin1"
password="@123"

otp=random.randint(1000,9999)
print(otp)
a=int((input('Enter otp:')))

if(username==user and password==p):
    if(otp==a):
        print('Login Successful')
    else:
        print('wrong otp entered')
else:
    print("LOgin failed!")
    print('please enter valid crecidential')
