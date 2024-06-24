#conversao
number = int(input('Enter a number: '))
choice = int(input('Now enter the conversion choice, 1 for binary, 2 for octal, and 3 for hexadecimal: '))

if choice == 1:
    binary = bin(number)[2:]
    print('The number {} converted to binary is {}'.format(number, binary))
elif choice == 2:
    octal = oct(number)[2:]
    print('The number {} converted to octal is {}'.format(number, octal))
elif choice == 3:
    hexadecimal = hex(number)[2:]
    print('The number {} converted to hexadecimal is {}'.format(number, hexadecimal))
else:
    print('You can only choose between 1, 2, and 3!')
