var=(int(input('Enter a number:')), int(input('Enter a number:')), int(input('Enter a number:')), int(input('Enter a number:')))
print(var)
quantity=0

for pos, i in enumerate(var):
    if i==9:
        quantity=quantity+1
        print(f'The number 9 appears {quantity} times.')
    if i==3:
        position=pos
        print(f'The number 3 is in position {position}')
    else:
        position=9
    if i%2==0:
        var= [i]
        print(f'The numbers pars is {var}')
if position==9:
    print('The number 3 is not present in the entered numbers')
    