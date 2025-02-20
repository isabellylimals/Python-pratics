SpellList = []

while True:
    print("[1] Add new spell")
    print("[2] Remove spell")
    print("[3] Show all spells")
    print("[4] Exit program")
    choice = int(input("Choose an option above: "))

    if choice == 1:
        spell = input("Enter the name of the spell:\n")
        SpellList.append(spell)

    elif choice == 2:
        spell_to_remove = input("What is the name of the spell you want to remove:\n")
        if spell_to_remove in SpellList:
            SpellList.remove(spell_to_remove)
            print(f"Spell {spell_to_remove} successfully removed\n")
        else:
            print(f"Spell {spell_to_remove} is not in the list, please check if you typed it correctly\n")

    elif choice == 3:
        print("List of spells:\n")
        for i, spell in enumerate(SpellList, start=1):
            print(f"Spell {i}: {spell}")

    elif choice == 4:
        print("Exiting the program...\n")
        break

    else:
        print("Invalid option. Please try again.\n")
