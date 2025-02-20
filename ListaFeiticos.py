# Explicação do Projeto: Lista de Feitiços
# Esse projeto permite ao usuário gerenciar uma lista de feitiços do universo de Harry Potter.
# O usuário pode adicionar, remover e visualizar os feitiços armazenados.

# Como funciona?
# O programa exibe um menu com opções:

# - Adicionar um feitiço
# - Remover um feitiço
# - Mostrar todos os feitiços
# - Sair do programa

# O usuário escolhe uma opção digitando um número correspondente.

# Caso escolha adicionar um feitiço, o usuário digita o nome do feitiço, que é armazenado na lista.

# Se quiser remover um feitiço, o usuário informa o nome do feitiço.
# Se ele estiver na lista, será removido; caso contrário, o programa avisa que não foi encontrado.

# Se optar por visualizar todos os feitiços, o programa exibe a lista completa.

# O programa continua rodando até o usuário escolher a opção de saída.
ListadeFeticos = []

while True:
    print("[1] Adicionar novo feitiço")
    print("[2] Remover feitiço")
    print("[3] Mostrar todos os feitiços")
    print("[4] Sair do programa")
    escolha = int(input("Escolha uma das opções acima: "))

    if escolha == 1:
        feitiço = input("Insira o nome do feitiço:\n")
        ListadeFeticos.append(feitiço)

    elif escolha == 2:
        feitico_remover = input("Qual o nome do feitiço que você quer remover:\n")
        if feitico_remover in ListadeFeticos:
            ListadeFeticos.remove(feitico_remover)
            print(f"Feitiço {feitico_remover} removido com sucesso\n")
        else:
            print(f"Feitiço {feitico_remover} não está presente na lista, verifique se digitou corretamente\n")

    elif escolha == 3:
        print("Lista de feitiços:\n")
        for i, feitiço in enumerate(ListadeFeticos, start=1):
            print(f"Feitiço {i}: {feitiço}")

    elif escolha == 4:
        print("Saindo do programa...\n")
        break

    else:
        print("Opção inválida. Tente novamente.\n")
