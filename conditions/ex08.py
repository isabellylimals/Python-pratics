#segmentos de um triangulo
seg1= float(input("Digite a medida do primeiro segmento:"))
seg2= float(input('Digite a medida do segundo sgemento:'))
seg3= float(input('Digite a medida do terceiro segmento:'))
if seg1+seg2>seg3 and seg1+seg3>seg2 and seg2+seg3>seg1:
    print('Esses segmentos podem formar um triangulo.')
else:
    print('Esses segmentos nao podem formar um triangulo.')