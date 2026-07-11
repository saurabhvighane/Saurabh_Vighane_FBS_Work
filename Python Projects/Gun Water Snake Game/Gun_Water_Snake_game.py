#   Gun Water Snake Game

import random

# Find out Winner
def winner(computer,user):
    if computer == user:
        return None

    elif computer == 's' and user == 'w':
        return False

    elif computer == 'w' and user == 'g':
        return False

    elif computer == 'g' and user == 's':
        return False

    else:
        return True

# How game work
print("--- Gun Water Snake Game ---")
print('Game will be best of 3')
print("Choose options:snake(s) water(w) gun(g)")
print()

user_score=0
computer_score=0

names = {
    "g": "Gun",
    "w": "Water",
    "s": "Snake"
}

for i in range(1,4):
    print(f'Round {i}')
    
    
    random_no = random.randint(1,3)

    if random_no==1:
        computer='s'
    elif random_no==2:
        computer='w'
    else:
        computer='g'

    user=(input("Your turn: (s)/(w)/(g): ")).lower()

    if user in ['g', 's', 'w']:

        result=winner(computer,user)
        print(f'You chose: {names[user]}')
        print(f'Computer chose: {names[computer]}')

        if result is None:
            print("It's a draw")
        elif result:
            print("You won this round!")
            user_score+=1
        else:
            print("You lose this round!")
            computer_score+=1
        

        # End match if any one wins first 2 round
        print(f'You scored: {user_score} | Computer scored: {computer_score}')
        print()
        if user_score==2 or computer_score==2:
            break
        
    
        
    else:
        print("Invalid input. Try again.") 
       
# show final result
print("- - - Final Result - - -")
print()

print(f'You scored: {user_score}')

print(f'computer scored: {computer_score}')

if user_score > computer_score:
    print("You Won the match!")

elif computer_score > user_score:
    print("Computer won the match!")

else:
    print("It's a draw!")
