values = []
values.append(int(input('Enter a value: ')))
choice = input('Do you want to continue? Y/N: ').upper()

while choice == 'Y':
    number = int(input('Enter a value: '))
    if number in values:
        print('This value already exists. It will not be added.')
    else:
        values.append(number)
    choice = input('Do you want to continue? Y/N: ').upper()

print(values)
