#custo de viagem
km = float(input('What is the distance of the trip? '))
if km <= 200.0:
    cost = 0.50 * km
    print("The cost of the trip is: {}R$".format(cost))
else:
    cost = km * 0.45
    print('The cost of the trip is: {}R$'.format(cost))
