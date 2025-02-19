"Dada uma lista de listas que representa notas de alunos, crie um programa que percorra essa estrutura e exiba apenas as notas que são maiores ou iguais a 7."

notas = [] 
escolha = int(input("Deseja adicionar uma nota? [1]Sim e [2]Não\n")) 

while escolha != 2:  
    nota = float(input("Insira a nota:\n"))  
    notas.append(nota)  
    escolha = int(input("Deseja adicionar uma nota? [1]Sim e [2]Não\n"))  


for i in notas:
    if i >= 7.0:  
        print("Notas maiores ou iguais a 7.0:", i)
        break  
else:
    print("Nenhuma nota é maior ou igual a 7.0.")