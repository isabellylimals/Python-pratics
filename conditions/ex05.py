#ano bissexto
ano= int(input('Digite o ano que deseja analisar:'))
if ano%400==0:
    print('O ano {} eh bissexto'.format(ano))
else:
    print('O ano {} nao eh bissexto.'.format(ano))