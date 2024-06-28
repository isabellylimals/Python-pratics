
import random
computer_choice = random.randint(0, 10)
sum = 0
victories = 0
losses = 0

while losses != 1:
    chosen_number = int(input('Choose a number from 0 to 10: '))
    even_or_odd = str(input('Even or odd? E/O: ')).upper()
    sum = chosen_number + computer_choice
    print(f'You played {chosen_number} and the computer {computer_choice} and the sum is {sum}')
    if even_or_odd == 'E' and sum % 2 == 0 or even_or_odd == 'O' and sum % 2 == 1:
        victories += 1
    else:
        losses += 1
        print('You lost :(')
        break
print(f'You had {victories} consecutive victories!')
