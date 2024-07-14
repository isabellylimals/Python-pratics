number= [2,4,1,5,4]
number[2]=3
#number.append(8)
number.sort()
number.insert(2,0) #coloca o 0 na posicao 2
if 4 in number:
    number.remove(4)
else:
    print("Numero nao achado..")
print(number)
print(f'Essa lsta tem {len(number)} elementos')