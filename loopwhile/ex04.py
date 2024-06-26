number = int(input('Enter a number to calculate its factorial: '))
while number != 0:
    factorial = 1
    print('{}! = '.format(number), end='')
    for i in range(number, 0, -1):
        factorial *= i
        if i > 1:
            print('{} x '.format(i), end='')
        else:
            print('1 = {}'.format(factorial))
    break

print('Exiting the program...')
