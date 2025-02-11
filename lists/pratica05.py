teste= list()
teste.append('Isa')
teste.append(20)
galera=list()
galera.append(teste[:])
teste[0]= 'MARIA'
teste[1]=22


galera2=[['Joao',25],['Isa',10]]
print(galera)
for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade')
    print(p[0])
galera3= list()
dado=list()
for c in range(0,3)
dado.append(str(input('Nome:')))
dado.append(int(input('IDADE:')))
galera3.append(dado[:])
print(galera3)
for p in galera2:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade')