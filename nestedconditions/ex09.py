#pagamentos
total_price = float(input('Enter the total purchase amount: '))
print('========= ANTIQUE STORE ============')
print('TOTAL PURCHASE AMOUNT:')
print('PAYMENT METHODS:')
print('[1] Cash or check')
print('[2] Credit card (one-time payment)')
print('[3] 2x on credit card')
print('[4] 3x or more on credit card')

choice = int(input('Which payment option would you like to choose? '))

if choice == 1:
    discount = (total_price * 10) / 100
    print('Your purchase of {:.2f}R$ is now {:.2f}R$ with a 10% discount.'.format(total_price, total_price - discount))
elif choice == 2:
    discount = (total_price * 5) / 100
    print('Your purchase of {:.2f}R$ is now {:.2f}R$ with a 5% discount.'.format(total_price, total_price - discount))
elif choice == 3:
    print('Your purchase remains the same at {:.2f}R$.'.format(total_price))
elif choice == 4:
    interest = (total_price * 20) / 100
    print('Your purchase of {:.2f}R$ is now {:.2f}R$ with 20% interest.'.format(total_price, total_price + interest))
else:
    print('Invalid choice. Please select a valid payment option.')
