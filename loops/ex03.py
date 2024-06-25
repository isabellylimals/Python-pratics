#contagem de multiplos de 1 ate 500
sum = 0
quantity = 0
for cont in range(1, 501):
    if cont % 3 == 0:
       sum = sum + cont
       quantity = quantity + 1

print('The sum of {} numbers divisible by 3 is: {}'.format(quantity, sum))
