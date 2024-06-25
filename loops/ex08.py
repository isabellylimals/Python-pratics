#palindromo
sentence = str(input('Enter any sentence: '))
words = sentence.split()
together = ''.join(words)
reverse = ''

for letter in range(len(together) - 1, -1, -1):
    reverse += together[letter]
    print(reverse)

if reverse == together:
    print('The sentence is a palindrome.')
else:
    print('The sentence is not a palindrome.')
