# Write a program to input any alphabet and check whether it is vowel or consonant.

a=input("Enter any alphabet: ")

if(a in 'aeiouAEIOU'):
    print("Alphabet is vowel")
else:
    print("Alphabet is consonant")