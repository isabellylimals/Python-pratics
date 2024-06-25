#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos
under_20 = 0
sum = 0
oldest_age = 0
oldest_name = str

for i in range(1, 4 + 1):
    name = str(input('Enter your name: '))
    age = int(input('Enter your age: '))
    sum += age
    gender = int(input('Enter your gender: 1 for female and 2 for male'))

    if gender == 2:
        if age > oldest_age:
            oldest_age = age
            oldest_name = name

    if gender == 1:
        if age < 20:
            under_20 += 1

average_age = sum / 4

print('The average age is: {}'.format(average_age))
print('The name of the oldest man is: {}'.format(oldest_name))
print('There are {} women under 20 years old.'.format(under_20))
