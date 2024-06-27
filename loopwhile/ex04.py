number = int(input('Enter a number to calculate its factorial: '))
print('{}! = '.format(number), end='')
count=number
factorial=1

while count> 0:
    print('{} x '.format(count), end='')
    print('' if count>1 else '=', end= '')
    factorial=factorial*count
    count= count-1
print('{}'.format(factorial))
print('Exiting the program...')
