
import random
number = random.randint(0, 9 + 1)
guess = int(input('What number do you think the machine chose? '))
while guess != number:
    print('Wrong guess :(')
    guess = int(input('Give another guess: '))
print('Congratulations, you guessed it!')
