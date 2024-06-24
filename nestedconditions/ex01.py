house_value = float(input('What is the house value? '))
salary = float(input('What is the buyer\'s salary? '))
years_to_pay = int(input('In how many years will the debt be paid off? '))
installment = house_value / (years_to_pay * 12)
allowed_percentage = (salary * 30) / 100

if installment > allowed_percentage:
    print('Loan denied. Installment exceeds the allowed value.')
elif installment <= allowed_percentage:
    print('Loan approved! The installment value will be {:.2f}R$ in {} years of financing.'.format(installment, years_to_pay))
