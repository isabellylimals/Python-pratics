produtos=('Lapis',1.50,
           'Caderno',25.50,
            'Borracha', 0.50,
            'Mochila', 50.00, 
            'Estojo', 15.10, 
            'Lapiseira', 5.50 )
print('-' *30)
print("Listagem de precos")
for pos in range(0,len(produtos)):
    if pos%2==0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:<15}')