#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
#
numbers = [[], []]  

for i in range(7):  
    value = int(input('Enter a number: '))
    if value % 2 == 0:
        numbers[0].append(value)  
    else:
        numbers[1].append(value)  

numbers[0].sort()
numbers[1].sort()

print(f'Even numbers in ascending order: {numbers[0]}')
print(f'Odd numbers in ascending order: {numbers[1]}')
