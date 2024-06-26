#tabuada
number = int(input('Choose a number to see its multiplication table: '))
print('MULTIPLICATION TABLE OF {}'.format(number))
for cont in range(0, 10 + 1):
    multiplication = cont * number
    print('{} x {} = {}'.format(number, cont, multiplication))
