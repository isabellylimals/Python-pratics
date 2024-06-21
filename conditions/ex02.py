#Ultrapassagem de velocidade e multa
velocidade=int(input("Informe a velocidade km/h do carro:"))
if velocidade>80:
    print('Você ultrapassou o limite de velocidade permitido e foi multado.')
    km_ultrapassados= 80-velocidade
    multa= km_ultrapassados*(-7)
    print('O valor da multa eh de {}R$:'.format(multa))
else:
    print('Você esta na velocidade correta!')
