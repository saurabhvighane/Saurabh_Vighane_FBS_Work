def square(num):
    return num**2   

# data = [1,2,3,4,5,6,7,8,9,10]


res = tuple(map(square,[10,20]))
print(type(res))
print(res)