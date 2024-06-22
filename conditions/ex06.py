#menor e maior valores
n1=int(input('Digite um valor:'))
n2=int(input('Digite um segundo valor:'))
n3= int(input('Digite um terceiro valor:'))

if n1 > n2 > n3:
    print('O menor número digitado é: {}'.format(n3))
    print('O maior número digitado é: {}'.format(n1))
elif n2 > n1 > n3:
    print('O menor número digitado é: {}'.format(n3))
    print('O maior número digitado é: {}'.format(n2))
else:
    print('O menor número digitado é: {}'.format(n1))
    print('O maior número digitado é: {}'.format(n2))
