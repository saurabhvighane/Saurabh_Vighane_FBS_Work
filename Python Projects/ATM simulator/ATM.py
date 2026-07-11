# check pin
# check balance
# deposite amount
# withdrow amount

pin=1234
ch=2
for i in range(3):
    upin=int(input("Enter pin:"))
    if upin==pin:
        print("Login Successful!")
        break
    else:
        print("Wrong pin! Login failed!")
        print(f'You have {ch} chances left')
        ch-=1
else:
    print("You are out of chances")