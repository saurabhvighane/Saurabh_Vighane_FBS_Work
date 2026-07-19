# To perform multiple operation on data and return only one value

import functools

data= [1,2,3,4,5,6,7,8,9,10]

res=functools.reduce(lambda a,b: a*b,data)

print(res)