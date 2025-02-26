#exemplo feito por IA
hogwarts_houses = {
    "Grifinória": "Coragem",
    "Sonserina": "Ambição",
    "Corvinal": "Sabedoria",
    "Lufa-Lufa": "Lealdade"
}
print(hogwarts_houses["Grifinória"])  # Saída: Coragem
print(hogwarts_houses.get("Sonserina", "Casa não encontrada"))  
# Saída: Ambição
hogwarts_houses["Puffskein"] = "Criatura fofa"  
print(hogwarts_houses)
hogwarts_houses["Puffskein"] = "Criatura fofa"  
print(hogwarts_houses)
del hogwarts_houses["Lufa-Lufa"]
for casa, qualidade in hogwarts_houses.items():
    print(f"{casa}: {qualidade}")
# Pedindo ao usuário para adicionar uma nova casa
nova_casa = input("Digite o nome da nova casa: ")
caracteristica = input(f"Digite a principal característica de {nova_casa}: ")

# Adicionando ao dicionário
hogwarts_houses[nova_casa] = caracteristica

# Mostrando o dicionário atualizado
print("\nDicionário atualizado:")