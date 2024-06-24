#alistamento militar
birth_year = int(input('Enter your year of birth: '))
current_year = int(input('Enter the current year: '))
age = current_year - birth_year

if age < 18:
    print('You were born in {} and are {} years old in {}'.format(birth_year, age, current_year))
    missing = 18 - age
    print('You still have {} years before you reach the right age to enlist.'.format(missing))
    print('Your enlistment will be in {}'.format(current_year + missing))
elif age > 18:
    print('You were born in {} and are {} years old in {}'.format(birth_year, age, current_year))
    overdue = age - 18
    print('You should have enlisted {} years ago.'.format(overdue))
    print('Your enlistment should have been in the year {}'.format(current_year - overdue))
elif age == 18:
    print('You were born in {} and are {} years old in {}'.format(birth_year, age, current_year))
    print('You are at the age to enlist. It is urgent that you enlist as soon as possible.')
else:
    print('Invalid input. Please enter valid years.')
