n1 = int(input('Enter a value: '))
n2 = int(input('Enter a second value: '))
n3 = int(input('Enter a third value: '))

smallest = n1
largest = n1

if n2 < smallest:
    smallest = n2
if n2 > largest:
    largest = n2

if n3 < smallest:
    smallest = n3
if n3 > largest:
    largest = n3

print('The smallest number entered is: {}'.format(smallest))
print('The largest number entered is: {}'.format(largest))
