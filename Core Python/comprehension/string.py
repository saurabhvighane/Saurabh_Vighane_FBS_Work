# By normal code
srt = 'firstbit'
new = srt.upper()
print(new)

# using comprehension
res = [i.upper() for i in srt]
print(res)


string = 'i am student'
words = string.split()
le = len(words)
print(le)
 # OR
li = ['I',"am",'good','in','python']
c = len(li)
print(c)

# a = [i for i in range(1,101) if i%2!=0]
# print(a)
for i in range(1,101):
    if i%2!= 0:
        print(i,"Odd no")
    else:
        print(i,"Even no")

li = ['Even' if i%2==0 else "Odd" for i in range(1,101)]
print(li)