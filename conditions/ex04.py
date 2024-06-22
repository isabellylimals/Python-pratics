#custo de viagem
km= float(input('Qual a distancia da viagem?'))
if km<=200.0:
    custo= 0.50*km
    print("O custo da viagem ficou de: {}R$".format(custo))
else:
    custo= km*0.45
    print('O custo da viagem ficou de: {}R$'.format(custo))