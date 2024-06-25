# Solicita ao usuário que digite um número de 1 a 9999
number = int(input('Enter a number from 1 to 9999:'))

# Obtém o dígito das unidades
unit = number // 1 % 10

# Obtém o dígito das dezenas
tens = number // 10 % 10

# Obtém o dígito das centenas
hundreds = number // 100 % 10

# Obtém o dígito dos milhares
thousands = number // 1000 % 10

# Imprime os resultados
print('Analyzing the number:')
print('Unit: {}'.format(unit))
print('Tens: {}'.format(tens))
print('Hundreds: {}'.format(hundreds))
print('Thousands: {}'.format(thousands))
