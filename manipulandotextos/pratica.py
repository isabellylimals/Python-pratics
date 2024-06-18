frase= '    Harry Potter é melhor que Senhor dos aneis'
print(frase[:25])
print(frase.upper().count())
print(frase)
print(len(frase.strip()))
frase=frase.replace('aneis', 'Aneis')
print(frase)
print(frase.find('video'))
dividido=(frase.split())
print(dividido[0][0]) #primeiro item da lista e primeira letra do primeiro nome
