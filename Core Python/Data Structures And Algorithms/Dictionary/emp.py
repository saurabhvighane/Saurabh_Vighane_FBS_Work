# add 20% sal 
dict = {"id":'',"name":"","address":''}
# dict['sal']+= (dict['sal']*20/100) 
# print(dict)

# wap to add 3 emp name,sal,address in dict

dict = {}
for i in range(1,4):
    name = input("enter the emp name:")
    sal = int(input("enter the salary of emp:"))
    add = input("enter the adress of emp:")
    dict[i]={ "name":name,"sal":sal,"address":add}    # store in form of dictionary
    dict[i]=[name,sal,add]      # store in form of list
print("emp details:")
# for i,j in dict.items():
#     print(i,j)
print(dict)
