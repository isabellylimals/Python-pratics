#SEno, cosseno e tangente usando bibliotecas do python
import math
numero=float(input('Digite um numero qualquer:')     )
numero= math.radians(numero)
seno= math.sin(numero)
cosseno= math.cos(numero)
tangente= math.tan(numero)
print("O seno de {:.2f} eh : {:.2f}". format(numero,seno))
print("O cosseno de {:.2f} eh : {:.2f}". format(numero,cosseno))
print("A tangente de {:.2f} eh : {:.2f}". format(numero,tangente))