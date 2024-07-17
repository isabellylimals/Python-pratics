
complete_list = []
even_list = []
odd_list = []
number = int(input("Enter a number: "))
if number % 2 == 0:
    even_list.append(number)
else:
    odd_list.append(number)
qt = 1
complete_list.append(number)

choice = int(input("Do you want to continue entering numbers? 0/NO 1/YES: "))
while choice == 1:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)
    qt += 1
    complete_list.append(number)
    choice = int(input("Do you want to continue entering numbers? 0/NO 1/YES: "))
    if choice != 1 and choice != 0:
        print("Invalid choice, only 0/NO and 1/YES are allowed")
print(f'Complete list: {complete_list}')
print(f'List with even numbers: {even_list}')
print(f'List with odd numbers: {odd_list}')
