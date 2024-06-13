# Car rental
days = int(input('For how many days was the car rented? '))
km = float(input('Enter the number of kilometers the car traveled: '))
price = (days * 60) + (km * 0.15)
print('The amount to pay for {:.2f} days and {:.2f} kilometers traveled is: {:.2f}'.format(days, km, price))
