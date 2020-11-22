import random

from players import Player
from card_deck import Card
from card_deck import Deck


# Este es el archivo base del juego. Es el que se ejecutará e irá llamando al resto de archivos.

print('Welcome to "Ass Card Game" (or ACG for friends)')

# Try y Except:

player_number = int(input("How many player are you?: "))

# Esta lista será usada para definir el orden del juego, aleatorizándola más adelante 
players = []

for i in range(player_number):  # Crear función de esto
    name = input(f"Say player {i+1} name: ")
    while True:
        if name not in players:
            players.append(name)
            players[i] = Player(name) # Funciona
            players[i].get_data() # Este método se encarga de hacer la introducción
            break
        else:
            print("That name is taken. Please, choose another one")


print("Let's begin the game!")

# Definición de baraja y barajarla
main_deck = Deck()
main_deck.shuffle()


while main_deck.deck != []:  # Crear función de esto
    for player in players:
        if main_deck.deck == []:
            break
        player.add_card(main_deck.deal())

for player in players:
    print("\nHi " + player.name + " this is your hand: \n")
    print(len(player.hand))
    for card in player.hand:
        print(card)
