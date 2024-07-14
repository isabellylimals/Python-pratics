###Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
values = []
count = 0
highest_value = 0
lowest_value = 100
for i in range(0, 5):
    values.append(int(input(f'Enter a value for position {count}:')))
    count = count + 1
for pos, num in enumerate(values):
    if num > highest_value:
        highest_value = num
        position = pos
    if num < lowest_value:
        lowest_value = num
        position2 = pos
print(f'The highest value is {highest_value} and it is in position [{position}] the lowest value is {lowest_value} and it is in position [{position2}].')
