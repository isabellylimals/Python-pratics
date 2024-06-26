number = int(input('Enter a number to calculate its factorial: '))
soma = 1

while number > 0:
    for i in range(number, 0, -1):
        print('{}! = {} x {}'.format(number, number, i))
        soma = soma * i
    break

print('The factorial of {} is: {}'.format(number, soma))
