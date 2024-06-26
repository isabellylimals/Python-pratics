#grupo de maioridade
legal_age_count = 0
minor_count = 0

for i in range(1, 7 + 1):
    birth_year = int(input('Enter your birth year: '))
    if 2024 - birth_year >= 18:
        legal_age_count += 1
    elif 2024 - birth_year < 18:
        minor_count += 1

print('There are {} legal adults and {} minors'.format(legal_age_count, minor_count))
