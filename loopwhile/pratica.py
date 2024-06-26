n=1
par=impar=0
while n!=0:
    n=int(input('Digite um numero:'))
    if n!=0:
        if n%2==0:
            par=par+1
        else:
            impar=impar+1
print('Voce digitou {} numeros pares e {} numeros impares:'.format)