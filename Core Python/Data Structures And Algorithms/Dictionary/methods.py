di = {'id': '100' , 'name':'Saurabh' , 'sal': '100000'}

di2 = di.copy()

print(di.get('id','key not found'))
print(di.items())
print(di.keys())
# print(di.pop('name'))
print(di.popitem()) # removes last key and value
print(di2.update({'add':21}))   # if key is present update the value otherwise create new key and value
print('di2',di2)
print(di.values())

di ['Add'] = 'Pune'
print(di)

