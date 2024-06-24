#classificando atletas
year_of_birth = int(input('Enter your year of birth: '))
age = 2024 - year_of_birth

if age <= 9:
    print('Classification: MIRIM, {} years old'.format(age))
elif 9 < age <= 14:
    print('Classification: INFANTIL, {} years old'.format(age))
elif 14 < age <= 19:
    print('Classification: JUNIOR, {} years old'.format(age))
elif 19 < age <= 25:
    print('Classification: SENIOR, {} years old'.format(age))
elif age > 25:
    print('Classification: MASTER, {} years old'.format(age))
else:
    print('Invalid input. Please enter a valid year of birth.')
