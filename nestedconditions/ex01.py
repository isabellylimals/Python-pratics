valor_casa= float(input('Qual o valor da casa?'))
salario= float(input('Qual o salario do comprador?'))
anospagar= int (input('Em quantos anos a divida sera quitada?'))
prestacao= valor_casa/(anospagar*12)
valorporcentagem= (salario*30)/100
if prestacao>valorporcentagem:
    print('Emprestimo negado. Prestacao exede o valor permitido.')
elif prestacao<valorporcentagem:
    print('Emprestimo aprovado! o valor da prestacao sera de {:.2f}R$ em {} anos de financiamento'.format(prestacao,anospagar))