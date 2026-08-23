# 3. Develop a function that counts the occurrences of each word in a given text. Use regular
# expressions to split the text into words and then count the frequency of each word.


import re


def count_words(text):

    words = re.findall(r'\b\w+\b', text.lower())

    frequency = {}

    for word in words:

        if word in frequency:
            frequency[word] += 1

        else:
            frequency[word] = 1

    return frequency


text = input("Enter text: ")

result = count_words(text)

print(result)