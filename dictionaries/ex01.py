"Crie um dicionário com feitiços e seus efeitos. Depois, peça ao usuário um feitiço e mostre o efeito correspondente."

feiticos={
    "Expelliamus": "Expulsa objetos",
    "Alohomora": "Abre portas",
    "Expecto Patronum": "Invoca um patrono",

}
feitico= input("Digite um feitiço:")
for feiticos, efeito in feiticos.items():
    if feiticos==feitico:
        print(f"{feiticos}: {efeito}")
    else:
        print("Fetiço não encontrado\n")
        