#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
highest_weight = 0.0
lowest_weight = 500.0

for i in range(1, 5 + 1):
    weight = float(input('Enter your weight: '))
    if weight < lowest_weight:
        lowest_weight = weight
    elif weight > highest_weight:
        highest_weight = weight

print('The highest weight is {:.2f}kg and the lowest is {:.2f}kg'.format(highest_weight, lowest_weight))
