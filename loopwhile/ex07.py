
terms = int(input('Quantos termos você quer mostrar? '))
first_term = 0
second_term = 1
print('Fibonacci: {} {}'.format(first_term, second_term), end=' ')

count = 2
while count < terms:
    next_term = first_term + second_term
    print('{}'.format(next_term), end=' ')
    
    first_term = second_term
    second_term = next_term
    
    count += 1
