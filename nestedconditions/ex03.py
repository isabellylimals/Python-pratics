#comparando numeros
n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))

if n1 > n2:
    print('The first number is greater than the second.')
elif n2 > n1:
    print('The second number is greater than the first.')
elif n1 == n2:
    print('Both numbers are equal.')
else:
    print('Invalid input. Please enter valid numbers.')
