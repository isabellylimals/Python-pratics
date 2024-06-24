#pedra papel e tesoura
import random
print('WELCOME TO ROCK PAPER SCISSORS')
print('Your options:')
print('[0] Rock')
print('[1] Paper')
print('[2] Scissors')

opponent_choice = random.randint(0, 2)
your_choice = int(input('ENTER YOUR CHOICE: '))

if your_choice == 1 and opponent_choice == 2:
    print('Your opponent chose scissors and you chose paper, you lost :(')
elif your_choice == 2 and opponent_choice == 1:
    print('You chose scissors and your opponent chose paper, CONGRATULATIONS YOU WON!')
elif opponent_choice == 0 and your_choice == 1:
    print('You chose paper and your opponent chose rock, CONGRATULATIONS YOU WON!')
elif opponent_choice == 1 and your_choice == 0:
    print('Your opponent chose paper and you chose rock, you lost :(')
elif your_choice == 0 and opponent_choice == 2:
    print('You chose rock and your opponent chose scissors, CONGRATULATIONS YOU WON!')
elif opponent_choice == 0 and your_choice == 2:
    print('You chose scissors and your opponent chose rock, you lost :(')
elif your_choice == opponent_choice:
    print('TIE, you both chose the same.')
else:
    print('Invalid choice. Please select 0, 1, or 2.')
