#ano bissexto
year = int(input('Enter the year you want to analyze: '))
if year % 400 == 0:
    print('The year {} is a leap year.'.format(year))
else:
    print('The year {} is not a leap year.'.format(year))
