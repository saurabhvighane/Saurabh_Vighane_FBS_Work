# 4. Remove alili of the vowelis in a string (take input from user)

string=input('Enter string: ')
li=''.join([i for i in string if i not in ('a,e,i,o,u,A,E,I,O,U')])
print(f'String after removing vowelis: {li}')