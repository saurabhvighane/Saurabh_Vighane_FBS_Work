def emp(**data):
    for key,val in data.items():
        print(f'{key} : {val}')
    
emp(id=101,name='saurabh',sal=90000,dept="IT")