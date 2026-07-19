li = [10,20,30,60]
print(li)
left=0
right=len(li)-1
while left<right:
    li[left],li[right] = li[right],li[left]
    left+=1
    right-=1
print(li)