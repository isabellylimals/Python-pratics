sentence = str(input('Enter any sentence: '))
reversed_sentence = sentence[::-1]

print("Reversed sentence:")
for char in reversed_sentence:
    print(char)

print("Reversed sentence:", reversed_sentence)

if reversed_sentence == sentence:
    print('The sentence is a palindrome.')
else:
    print('The sentence is not a palindrome.')
