frase=str(input('EScreva uma frase qualquer:'))
frase=frase.strip()
maiuscula= frase.upper()
letraA= maiuscula.count('A')
posicao= maiuscula.find("A")
last_posicao= frase.rfind('A')
print('A letra A aparece {} vezes na sua frase.'.format(letraA))
print('A primeira letra A esta na posicao {}:'.format(posicao))
print('A ultima ocorrencia da letra A {} esta na posicao:'.format(last_posicao))