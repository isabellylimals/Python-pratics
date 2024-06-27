count = 1
choice = 1

print('=== 10 terms of an AP ===')
first_term = int(input('Enter the first term: '))
common_difference = int(input('Now enter the common difference: '))
print('AP: {}'.format(first_term), end='')

aux = first_term
aux02 = 10

while choice != 0:
    if count < aux02:
        proxterm = aux + common_difference
        aux = proxterm
        print(' {}'.format(aux), end='')
        count += 1
    else:
        choice = int(input('How many more terms would you like to add? '))
        if choice == 0:
            break
        else:
            aux02 += choice

