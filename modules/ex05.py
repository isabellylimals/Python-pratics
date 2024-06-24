import random

nome1 = input('Digite o nome do primeiro aluno:')
nome2 = input('Digite o nome do segundo aluno:')
nome3 = input('Digite o nome do terceiro aluno:')
nome4 = input('Digite o nome do quarto aluno:')

lista = [nome1, nome2, nome3, nome4]  
random.shuffle(lista) 
print("A ordem sorteada de alunos foi: {}".format(lista)) 
