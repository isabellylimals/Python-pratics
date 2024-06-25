#numeros primos
count = 0
number = int(input('Type a number: '))
for i in range(1, 10 + 1):
    if number % i == 0:
        count=count + 1

if count == 2:
    print('The number {} is only divisible by itself and 1, so it is prime.'.format(number))
else:
    print('The number {} is divisible {} times between 1 and 10, so it is not prime.'.format(number, count))
