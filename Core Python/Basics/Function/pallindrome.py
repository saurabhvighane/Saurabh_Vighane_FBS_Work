def ispallindrome(no):
    t=no
    rev=0
    while(t>0):
        d=t%10
        t//=10
        rev=rev*10+d
    if(rev==no):
        return True
    else:
        return False

n=int(input("Enter no: "))
if(ispallindrome(n)):
    print("no is pallindrome")
else:
    print("No is not pallindrome")