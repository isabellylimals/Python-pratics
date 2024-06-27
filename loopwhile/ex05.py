#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
count = 1
print('=== 10 terms of an AP ===')
first_term = int(input('Enter the first term: '))
common_difference = int(input('Now enter the common difference: '))
print('AP: {}'.format(first_term), end='')

aux = first_term
while count < 10:
    proxterm = aux + common_difference
    aux = proxterm
    print(' {}'.format(aux), end='')
    count = count + 1
