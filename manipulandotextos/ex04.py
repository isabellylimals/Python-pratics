#verificar se tem um sobrenome dentro do nome da pessoa, se tiver retorna 1 se nao tiver retorna 0
nome=str(input('Digite seu nome completo'))
nome.strip()
print('Seu nome tem Silva?',nome.count('Silva'))
verificar= 'Lima' in nome
print('Seu nome tem Lima?{}'.format(verificar))