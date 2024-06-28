
print('====================')
print(' LOJAO TEM DE EVERYTHING')
print('====================')
total = 0
qtd = 0
cheapest_price = 50000
product_name = ""

while True:
    name = input('Enter the product name: ').capitalize()
    price = float(input('Enter the product price: '))
    choose = input('Do you want to continue? Y/N: ').upper()
    total += price
    if price > 1000:
        qtd += 1
    if price < cheapest_price:
        cheapest_price = price
        product_name = name
    if choose == 'N':
        break

print('The total expense was {:.2f} R$'.format(total))
print(f'{qtd} products cost more than 1000 R$')
print(f'The cheapest product was {product_name}')
