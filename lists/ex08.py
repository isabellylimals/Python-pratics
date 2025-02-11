##Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
people = []  
count = 0  
heaviest = [] 
lightest = []  
max_weight = 0  
min_weight = float('inf')  

choice = int(input('Do you want to register a person? 1 for NO, 2 for YES: '))

while choice != 1:
    name = input("Enter the person's name: ")
    weight = float(input("Enter the person's weight: "))
    
    people.append([name, weight])  
    count += 1  

    if weight > max_weight:
        max_weight = weight
        heaviest = [[name, weight]]  
    elif weight == max_weight:
        heaviest.append([name, weight])  
    
    if weight < min_weight:
        min_weight = weight
        lightest = [[name, weight]]  
    elif weight == min_weight:
        lightest.append([name, weight])  

    choice = int(input('Do you want to register another person? 1 for NO, 2 for YES: '))

print(f'\nTotal number of registered people: {count}')

print("\nHeaviest person(s):")
for person in heaviest:
    print(f'Name: {person[0]}, Weight: {person[1]} kg')

print("\nLightest person(s):")
for person in lightest:
    print(f'Name: {person[0]}, Weight: {person[1]} kg')
