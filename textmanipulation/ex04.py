#verificar se tem um sobrenome dentro do nome da pessoa, se tiver retorna 1 se nao tiver retorna 0
nome = str(input('Enter your full name'))
nome.strip()
print('Does your name have Silva?', nome.count('Silva'))
verificar = 'Lima' in nome
print('Does your name have Lima?{}'.format(verificar))
