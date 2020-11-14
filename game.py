import random

from players import Player
from card_deck import Card
from card_deck import Deck


# Este es el archivo base del juego. Es el que se ejecutará e irá llamando al resto de archivos.

print('Welcome to "Ass Card Game" (or ACG for friends)')

# Hay que encontrar una manera de evitar que el usuario introduzca valores extraños

player_number = int(input("How many player are you?: "))

# Esta lista será usada para definir el orden del juego, aleatorizándola más adelante 
players = []

for i in range(player_number):
    name = input(f"Say player {i+1} name: ")
    while True:
        if name not in players:
            players.append(name)
            name = Player(name) ###################### Esto hay que corregirlo!!! Creo que no funciona así, es lo que dijo Pablo
            #################### Sobreescribe el objeto "name" cada vez que itera: Demostración en línea 45
            name.get_data() # Este método se encarga de hacer la introducción
            break
        else:
            print("That name is taken. Please, choose another one")


main_deck = Deck()
main_deck.shuffle()

# Reparto de cartas:
'''
while main_deck.deck != []:
    for i in players:
        players[i].add_card(main_deck.deal())

for card in players[1].hand:
    print(card)
'''
# No funciona, hay que corregir. Da error en la línea 38. Probar para ver
print(players)
name.get_data(3)


##Ideas para solucionarlo: crear un generador que en función del número de jugadores cree una lista: [Player1, Player2, Player3...]