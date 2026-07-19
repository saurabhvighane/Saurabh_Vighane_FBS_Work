str="FirstBit Solutions"

print(str[:5])
print(str.capitalize())
print(str.count('s'))
# print(str.endswith('ns'))
print(str.find('Bit'))   # return -1 if not availiable  if availiable returns index
print(str.index('r'))      # return index if availiable otherwise give error
print(str.isalnum())    # alpha or numeric if avaliable return true otherwise false
print(str.isalpha())
print(str.isnumeric())
print(str.isdigit())
print(str.islower())
print(str.isspace())
print(' '.isspace())
print(str.isupper())
print("@".join(['a','b','c']))
print(str.lower())
print(str.replace('Bit','Bite'))
print(str.split(' '))
print(str.startswith('Fir'))
str1= '    [st] '
print(str1)
print(str1.strip())  # removes space from start and end
print(str.swapcase())  # convert whole string capital to small and vise versa
print(str.title())      # convert string word first letter small to capital and vise versa
print(str.upper())
print(str.lower())

# sr='["122.9.0,9","222.9.3.5"]'
# sr2=sr.strip('[],",')
# print(sr2)
# sr3=sr2.split(',')
# print(sr3)