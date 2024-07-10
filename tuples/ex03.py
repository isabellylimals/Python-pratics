import random
largest = 0
smallest = 10
var = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(var)
for count in var:
    if count > largest:
        largest = count
    if count < smallest:
        smallest = count
print(f'The largest number is: {largest} and the smallest is {smallest}')

#import random
#maior=0
#menor=10
#var= (random.randint(1,10), random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
#print(var)
#for count in range(len(var)):
 #   if var[count]>maior:
  #      maior= var[count]
   # if var[count]<menor:
    #    menor=var[count]
#print(f'O maior numero eh: {maior} e o menor eh {menor}')