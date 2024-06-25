#pa
print('=== 10 terms of an AP ===')
first_term = int(input('Enter the first term: '))
common_difference = int(input('Now enter the common difference: '))
for i in range(first_term, 20, common_difference):  # Note that 20 is the number of times the loop will repeat
    print(i)
