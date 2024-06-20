name = str(input('Enter your full name:'))
name = name.strip()
name_split = name.split()
first_name = name_split[0]
last_name = name_split[-1]
print('The first name is: {}'.format(first_name))
print("The last name is: {}". format(last_name))
