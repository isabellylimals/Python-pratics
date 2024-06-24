nome= str(input('Qual seu nome?'))
if nome=='Isabelly':
    print('Lindo nome')
else:
    print("\033[1;31;40mSeu nome eh muito normal\033[0m")
print("Bom dia, {}".format(nome))