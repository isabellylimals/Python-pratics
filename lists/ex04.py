normallist= []
number = int(input("Enter a number: "))
qt = 1
normallist.append(number)

choice = int(input("Do you want to continue entering numbers? 0/NO 1/YES: "))
while choice == 1:
    number = int(input("Enter a number: "))
    qt += 1
    normallist.append(number)
    choice = int(input("Do you want to continue entering numbers? 0/NO 1/YES: "))
    if choice != 1 and choice != 0:
        print("Invalid choice, only 0/NO and 1/YES are allowed")

print(f'The number of values entered: {qt}')

normallist.sort(reverse=True) # sort in descending order
print("List in descending order:", normallist)
if 5 in normallist:
    print("The number 5 is in the list")
else:
    print("The number 5 is not in the list")
