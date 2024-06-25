#soma dos pares
soma = 0
qtd = 0
for cont in range(1, 6 + 1):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma = soma + numero
        qtd = qtd + 1

print('Foram digitados {} números pares, e a soma deles é {}'.format(qtd, soma))
