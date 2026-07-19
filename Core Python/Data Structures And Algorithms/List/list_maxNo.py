li=[20,32,90,77,11]

max=li[0]

for i in range(1,len(li)):
    if li[i] > max:
        max = li[i]
print("Maximum no is:",max)