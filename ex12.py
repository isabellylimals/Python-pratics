# Product on sale with a 5% discount
regular_price = float(input('What is the price of the product? '))
discount = (regular_price * 5.0) / 100.0
price_with_discount = regular_price - discount
print('The product that cost {:.2f}R$ is now {:.2f}R$ with a 5% discount.'.format(regular_price, price_with_discount))
