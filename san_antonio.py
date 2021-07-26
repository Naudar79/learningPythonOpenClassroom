# -*- coding: utf8 -*-

quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre"]
characters = ["alvin et les chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "kirikou"]
def show_random_quote(my_list):
    item = my_list[0]
    return item

user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter. ")


while user_answer != "B":
    print(show_random_quote(quotes))
    user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter. ")

for character in characters:
    a_character = character.capitalize()
    print(a_character)

print(show_random_quote(quotes))