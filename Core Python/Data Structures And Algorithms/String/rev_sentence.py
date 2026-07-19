str = 'I am good in coding'

str2=str.split()
rev=''
for i in range(len(str2)-1,-1,-1):
    print(str2[i],end=" ")


# without using split funtion
str = 'I am good in coding'

word = ''
rev = ''

for i in str:
    if i != " ":
        word = word + i
    else:
        if rev == '':
            rev = word
        else:
            rev = word + " " + rev
        word = ""

if rev == '':
    rev = word
else:
    rev = word + " " + rev

print(rev)