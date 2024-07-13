##Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
words = ('Balde', 'Pessoa', 'Correr', 'Eu', 'Socorro')
vowels = 'aeiouAEIOU'

for word in words:
    if isinstance(word, str):
        vowels_in_word = []
        for letter in word:
            if letter in vowels and letter not in vowels_in_word:
                vowels_in_word.append(letter)
        if vowels_in_word:
            print(f'The word {word} has vowels: {", ".join(vowels_in_word)}')
