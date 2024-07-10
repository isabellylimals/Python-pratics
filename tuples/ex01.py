var = ('zero', 'one', 'two', 'three', 'four', 'five',
       'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
number = int(input('Enter a number from 0 to 20:'))
for count in range(len(var)):
    if count == number:
        print(var[count])
        break
print('Invalid number, only numbers from 0 to 20 are allowed')
