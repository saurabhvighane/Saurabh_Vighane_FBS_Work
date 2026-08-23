# 1. Develop a function that takes a text and a list of forbidden words. Replace all
# occurrences of these forbidden words with asterisks (*) using regular expressions.

import re


def replace_forbidden_words(text, forbidden_words):

    pattern = r'\b(' + '|'.join(forbidden_words) + r')\b'

    result = re.sub(
        pattern,
        lambda match: '*' * len(match.group()),
        text,
        flags=re.IGNORECASE
    )

    return result


text = input("Enter text: ")

forbidden_words = input(
    "Enter forbidden words separated by space: "
).split()

print("Original Text:", text)

print(
    "Updated Text:",
    replace_forbidden_words(text, forbidden_words)
)