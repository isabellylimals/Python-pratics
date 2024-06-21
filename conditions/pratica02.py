nota1= float(input("Digite a primeira nota desse aluno:"))
nota2= float (input('Digite a segunda nota desse aluno:'))
nota3= float(input('Digite a terceira nota desse aluno:'))
media= (nota1+nota2+nota3)/3
if media<7.0:
    print("REPROVADO")
else:
    print('APROVADO')
print('===FIM===')