# 6. Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)

string=input("Enter String: ")
dic={i: len(i) for i in string.split() }
print(dic)