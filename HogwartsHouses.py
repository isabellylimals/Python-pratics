import random

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

name = input("Enter your name: ")
house = random.choice(houses)

print(f"{name}, you have been sorted into {house}!")
