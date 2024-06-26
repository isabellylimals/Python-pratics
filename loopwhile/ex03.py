n1 = int(input("Enter the first value: "))
n2 = int(input("Enter the second value: "))
print('Options:')
print('[1] Add')
print('[2] Multiply')
print('[3] Find the larger number')
print('[4] Enter new numbers')
print('[5] Exit the program')
choice = int(input('Choose an option: '))
while choice != 5:
    if choice == 1:
        sum_result = n1 + n2
        print("The sum of the two numbers is: {}".format(sum_result))
        break
    if choice == 2:
        product = n1 * n2
        print('The product of the two numbers is: {}'.format(product))
        break
    if choice == 3:
        if n1 > n2:
            print('The larger number is: {}'.format(n1))
        else:
            print('The larger number is: {}'.format(n2))
        break
    if choice == 4:
        n1 = int(input("Enter the new first value: "))
        n2 = int(input("Enter the new second value: "))
        break
    if choice == 5:
        print('Exiting the program')
        break
    if choice not in [1, 2, 3, 4, 5]:
        print('Choose a valid option:')
        choice = int(input('Choose an option: '))
