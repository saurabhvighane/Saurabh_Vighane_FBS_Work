li = [10,20,30,40,50,60]

a=li[0]
print(a)
print(li[-1])
print(li[len(li)-1])
print(len(li))


sum=0
# method 1
for val in li:
    sum+=val
print(sum)
sum=0
# method 2 (mostly used)
for i in range(len(li)):
    sum+=li[i]
print(sum)