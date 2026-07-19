def conqure(li,start,mid,end):
    temp=[]
    left = start     
    right = mid+1
    while left<=mid and right<=end:
        if li[left]<li[right]:
            temp.append(li[left])
            left+=1
        else:
            temp.append(li[right])
            right+=1
    while left<=mid:
        temp.append(li[left])
        left+=1
    while right<=end:
        temp.append(li[right])
        right+=1
    k=start
    for i in temp:
        li[k]=i
        k+=1
    
def divide(li,start,end):
    if start<end:
        mid = (start+end)//2
        divide(li,start,mid)
        divide(li,mid+1,end)
        conqure(li,start,mid,end)

li = [9,22,9,99,11,34,7]
print("Before swapping:",li)
divide(li,0,len(li)-1)
print("After swapping:",li)

for i in range(len(li)-1,-1,-1):
    print(li)

