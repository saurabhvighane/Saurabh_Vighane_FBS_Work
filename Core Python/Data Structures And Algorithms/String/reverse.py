str=input("Enter string to reverse it:")
rev=''
for i in str: # for i in range(len(s)-1,-1,-1):
    rev= i+rev      #rev+=s[i]
print("Reverse:",rev)

if rev==str:
    print("String is palindrome")
else:
    print("String is not palindrome")