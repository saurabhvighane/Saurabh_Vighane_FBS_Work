# 5. Find all of the words in a string that are less than 5 letters (take input from user)

string=input("Enter string: ")
words=len([i for i in string.split() if len(i)<5])
print(f'words in given string "{string}" less than 5 letters are :{words}')