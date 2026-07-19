data=[1,2,3,4,5,6,7,8,9,10]

res=list(filter(lambda x :x%2==0,data))

print(res)

res=list(filter(lambda x: x**2,data))
print(res)