def add(*num):
    sum=0
    for val in num:
        sum+=val
    return sum

res=add(20,10,30,40,50)
res=add(90,88,12,32,1,3,4,5,2,9,9,1,0,4)
print(res)
