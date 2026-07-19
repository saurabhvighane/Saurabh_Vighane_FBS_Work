def digsep(num):
    if num>0:
        d=num%10
        print(d)
        digsep(num//10)
        

digsep(513)