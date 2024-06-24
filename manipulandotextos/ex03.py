#verificar se existe a letra 's' na primeira palavra
city = str(input('Which city were you born in? '))
city.strip()
print(city.lower().count('s'))
print(city[:1].lower() == 's')
