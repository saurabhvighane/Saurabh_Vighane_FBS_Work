def selection(li):
    size=len(li)
    for i in range(0,size-1):
        min_ind = i
        for j in range(i+1,size):
            if li[min_ind] > li[j]:
                min_ind = j
            li[i],li[min_ind] = li[min_ind],li[i]
        print(li)


li=[2,8,8,3,55,32] 
print("Before sort:",li)
selection(li)
print("After sort:",li)    
