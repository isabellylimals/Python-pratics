from math import sqrt
cateto_o=float(input('Digite o valor do cateto oposto:'))
cateto_a=float(input('Digite o valor do cateto adjacentr:'))
hipotenusa= sqrt((cateto_a*cateto_a)+(cateto_o*cateto_o))
print('A hipotenusa eh: {:.2f}'.format(hipotenusa))
#obs:poderia ter sido usada a biblioteca math.hypo, porem para aumentar um pouco o uso da logica preferi fazer assim