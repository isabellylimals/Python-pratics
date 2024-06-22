#conversao
numero= int(input('Digite um numero:'))
escolha= int(input('Agora digite a escolha da conversao, 1 para binario, 2 para octal e 3 para hexadecimal:'))
if escolha == 1:
    binario= bin(numero)[2:]
    print('O numero {} convertido para binario fica {}'.format(numero,binario))
elif escolha==2:
    n_octal=oct(numero)[2:]
    print('O numero {} convertido para octal fica {}'.format(numero,n_octal))
elif escolha==3:
    hexadecimal= hex(numero)[2:]
    print('O numero {} convertido para hexadecimal fica: {}'.format(numero,hexadecimal))
else:
    print('Voce so pode escolher entre 1,2 e 3!!')
    