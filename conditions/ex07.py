#aumento de salario
salario=float(input('Digite qual seu salario:'))
if salario<=1250.0:
    aumento= (salario*15)/100
    salario_novo= salario+aumento
    print('Seu salario de {}R$ teve um aumento de {}R$ e ficou {}R$.'.format(salario,aumento,salario_novo))
else:
    aumento= (salario*10)/100
    salario_novo= salario+aumento
    print('Seu salario de {}R$ teve um aumento de {}R$ e ficou {}R$.'.format(salario,aumento,salario_novo))