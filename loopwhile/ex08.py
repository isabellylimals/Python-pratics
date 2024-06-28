
condition = int
sum = 0
count = 0
while condition != 999:
    number = int(input('Type a number: or 999 to end the program: '))
    condition = number
    count = count + 1
    sum = sum + number
    if number == 999:
        new_sum = 999 - sum
        new_sum = -1 * (new_sum)

print('You entered {} numbers and their sum is {}'.format(count - 1, new_sum))
