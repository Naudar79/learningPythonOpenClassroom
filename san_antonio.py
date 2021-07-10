# -*- coding: utf8 -*-

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre"]

characters = ["alvin et les chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "kirikou"]

# show random quote
if user_answer == "B":
    pass
elif user_answer == "C":
    print("C pas la bonne réponse ! et G pas d'humour, je C...")
else:
  
    def show_random_quote(my_list):
        quote = my_list[0]
        print(quote)

show_random_quote(quotes)