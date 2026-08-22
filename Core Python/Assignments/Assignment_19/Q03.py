# 3. Count the number of spaces in a string (take input from user)

string = input("Enter a string: ")

spaces = [i for i in string if i == ' ']

print(f'No of spaces: {len(spaces)}')