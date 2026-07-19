def linearSearch(li,element):
    for i in range(len(li)):
        if li[i]==element:
            return i
    # else:
    #     return -1
    return -1    #same as above

ele=int(input("Enter no to search"))
li=[10,20,30,40,40,50,60,70]

res=linearSearch(li,ele)
if res!=-1:
    print(f'{ele} is present at position {res}')
else:
    print(f'{ele} is not present')


