# Solicita ao usuário que digite seu nome completo
name = str(input('Enter your full name:'))

# Converte o nome para letras maiúsculas
uppercase = name.upper()

# Converte o nome para letras minúsculas
lowercase = name.lower()

# Remove os espaços em branco no início e no final do nome
name = name.strip()

# Divide o nome em uma lista de palavras
divided = name.split()

# Obtém o primeiro nome (a primeira palavra da lista)
first_name = divided[0]

# Conta o número de caracteres no primeiro nome
count_first_name = len(first_name)

# Junta todas as palavras da lista sem espaços
divided = ''.join(divided)

# Conta o número total de caracteres no nome (sem espaços)
count_total = len(divided)

# Imprime o nome em letras maiúsculas
print('The name in uppercase: {}'.format(uppercase))

# Imprime o nome em letras minúsculas
print('The name in lowercase: {}'.format(lowercase))

# Imprime o número total de caracteres no nome (sem espaços)
print('The entire name has {} characters'.format(count_total))

# Imprime o número de caracteres no primeiro nome
print('The first name has {} characters'.format(count_first_name))
