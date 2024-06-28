qtd_men = 0
people_count = 0
women_under_20_count = 0

while True:
    sex = input('Enter your gender: F/M ').upper()
    age = int(input('Enter your age: '))
    people_count += 1
    
    if sex == 'M':
        qtd_men += 1
        
    if sex == 'F' and age < 20:
        women_under_20_count += 1
        
    choice = input('Do you want to continue registering people? Y/N ').upper()
    
    if choice == 'N':
        break

print(f'The quantity of men is: {qtd_men}')
print(f'The total number of people is: {people_count}')
print(f'The quantity of women under 20 years old is: {women_under_20_count}')
