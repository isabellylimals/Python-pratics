valores=[]
valores.append(5)
valores.append(4)
valores.append(3)
for pos, v in enumerate(valores):
    print(f'Na posicao {pos} foi encontrado {v}')
for cont in range(0,5):
    valores.append(int(input('Digite um valor:')))
a=[1,2,3,4]
b= a
b[2]=8 #muda a lista a tbm porque o phyton cria uma ligacao entre elas
#b=a[:] nao cria uma ligacao