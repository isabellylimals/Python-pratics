
number = int(input('Enter a number: '))
sum = number
smallest = number
largest = number
count = 1
choice = str(input('Do you want to continue entering values? (Y for yes and N for no): ')).upper()

if choice == 'Y':
    while choice != 'N':
        number = int(input('Enter a number: '))
        choice = str(input('Do you want to continue entering values? (Y for yes and N for no): ')).upper()

        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
        sum = sum+ number
        count= count+ 1

if choice == 'N':
    average = sum / count
    print('The smallest number entered was: {} and the largest was {}'.format(smallest, largest))
    print('The average of the values is {}'.format(average))
