"""
Project: Password Strength Checker & Generator

Description:
Checks password strength based on length, uppercase letters,
lowercase letters, digits, and special characters.
It can also generate a strong random password.

Language: Python
"""

import random

# check length of the password
def len_checker(pw):
    length = len(pw)
    if length >= 8:
        return True
    else:
        return False


# check upper character is present or not
def check_upper(pw):
    found = False
    for ch in pw:
        if ch.isupper():
            found = True
            break

    if found:
        return True
    else:
        return False


# check lower character is present or not in password
def check_lower(pw):
    found = False
    for ch in pw:
        if ch.islower():
            found = True
            break

    if found:
         return True
    else:
        return False


# check  digit is present or not in password
def check_digit(pw):
    found = False
    for ch in pw:
        if ch.isdigit():
            found = True
            break

    if found:
        return True
    else:
        return False


# check synbol is present or not in password
def check_special(pw):
    found = False
    special = """~`!@#$%^&*()_-+={}[];:'"<>,./?"""
    for ch in pw:
        if ch in special:
            found = True
            break

    if found:
        return True
    else:
        return False


# count the score of password
def score_checker(password):
    score = 0
    if len_checker(password):
        score += 1
    if check_upper(password):
        score += 1
    if check_lower(password):
        score += 1
    if check_digit(password):
        score += 1
    if check_special(password):
        score += 1
    return score


# give suggetions according to given password
def suggestions(password):
    print("\nSuggestions:")
    if not len_checker(password):
        print("Increase the password length to at least 8 characters")
    if not check_upper(password):
        print("Add at least 1 upper character")
    if not check_lower(password):
        print("Add at least 1 lower character")
    if not check_digit(password):
        print("Add at least 1 digit")
    if not check_special(password):
        print("Add at least 1 special symbol")


# calculate strength using score count
def strength(password):
    score = score_checker(password)
    if score <=2:
        print("Password strength: weak")
        print(f'score is {score}/5')  
    elif  3<= score <= 4:
        print("Password strength: medium")
        print(f'score is {score}/5')  
    else:
        print("Password strength: strong")
        print(f'score is {score}/5')  

    if score == 5:
        print("👌Excellent! Your password is strong")
    else:
        suggestions(password)


# Generates new strong password 
def pass_generator():
    length=int(input("Enter length of password: "))
    if length < 8:
        print("password length must be at least 8")
    else:
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        digits = '0123456789'
        special = "!@#$%^&*"
        password =""
        all_characters = uppercase + lowercase + digits + special
        password += random.choice(uppercase) + random.choice(lowercase) + random.choice(digits) + random.choice(special) 
        for i in range(length-4):
            password += (random.choice(all_characters))
        password_list=list(password)
        random.shuffle(password_list)
        password = "".join(password_list)
        print(password)
        print("\nCheking password strength...")
        strength(password)


# shows menu to select options
while True:
    print('\n======= Password Strength Checker ======')
    print("1.Check password strength")
    print('2.Generate password')
    print("3.Exit")
    choice = int(input("\nEnter your choice as (1-3): "))
    if choice == 1:
        password = input("\nEnter your  password to check strength: ")
        strength(password)
    elif choice == 2:
       pass_generator()
    elif choice == 3:
        print("Thanks for using password generator and strength checker")
        break
    else:
        print("Invalid choice! Try again")


