
sum = 0
count = 0
while True:
    number = int(input('Enter a number: '))
    if number == 999:
        break
    sum += number
    count += 1
print(f'The sum of the numbers is: {sum}')
print(f'The count of numbers is: {count}')
