import random
#Jogo simples de adivinhação :D
num= random.randint(0,5)
n_escolhido= int (input('Qual numero de 0 a 5 voce acha que o computador escolheu?'))
if n_escolhido==num:
    print('Parabéns você acertou!!')
else:
    print('Voce errou :( ')
print("FIM DE JOGO, ESPERO QUE TENHA SE DIVERTIDO :D")