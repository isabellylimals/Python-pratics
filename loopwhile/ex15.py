print('=' *30)
print('{:^30}'.format('BANCO PERDEU TUDO'))
print('=' *30)
withdraw_amount = int(input('How much do you want to withdraw? '))
total = withdraw_amount
bill = 50
total_bills = 0

while total > 0:
    if total >= bill:
        total -= bill
        total_bills += 1
    else:
        if total_bills > 0:
            print('You used {} bill(s) of ${:.2f}'.format(total_bills, bill))
        
        if bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 1
        
        total_bills = 0