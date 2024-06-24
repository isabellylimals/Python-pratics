import random

num = random.randint(0, 5)
chosen_number = int(input('Which number from 0 to 5 do you think the computer chose? '))

if chosen_number == num:
    print('Congratulations, you got it right!!')
else:
    print('You missed it :( ')
    
print("END OF GAME, HOPE YOU HAD FUN :D")
