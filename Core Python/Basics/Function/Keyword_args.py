def emp(id,sal,name,dept):
    data= f'ID:{id}\nSALARY:{sal}\nNAME:{name}\nDEPARTMENT:{dept}'
    return data

res=emp(101,name="Adinath",sal=50000,dept="IT")
print(res)