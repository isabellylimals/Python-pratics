cont=1
number=int(input('Quer ver a tabuada de qual numero?'))
while True:
    print('{} x {}= {}'.format(number,cont,number*cont))
    cont=cont+1
    if cont==11:
        number=int(input('Quer ver a tabuada de qual numero?'))
        if number==0:
            break
        else: 
            cont=1
            print('{} x {}= {}'.format(number,cont,number*cont))
            cont=cont+1