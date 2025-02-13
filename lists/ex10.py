##Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [] 
for i in range(3):
    linha = []  
    for j in range(3):
        n = int(input(f"Insira o número para a posição ({i+1}, {j+1}): "))
        linha.append(n)
    matriz.append(linha)

print("\nMatriz 3x3:")
for linha in matriz:
    print(" ".join([str(num) for num in linha]))
