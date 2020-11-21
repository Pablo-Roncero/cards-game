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
            players[i] = Player(name) ###################### Esto hay que corregirlo!!! Creo que no funciona así, es lo que dijo Pablo
            #################### Sobreescribe el objeto "name" cada vez que itera: Demostración en línea 45
            players[i].get_data() # Este método se encarga de hacer la introducción
            break
        else:
            print("That name is taken. Please, choose another one")

# Para solucionar el problema de la asignación de la variable a la instanciación de la clase Player,
# he añadido la posición que ocupa en el juego el jugador al nombre de la variable, por ej: players0,
# players1, etc. No es probablemente la mejor solución, pero creo que por ahora valdría.


print("Let's begin the game!")


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
# Creo que hay un problema con el bucle while, ya que repite cartas que ya han sido asignadas
# Tampoco consigo que pase al siguiente jugador

while main_deck.deck != []:
    for players[i] in players:
        print("\nHi " + players[i].name + " this is your hand: ")
        players[i].add_card(main_deck.deal())
        for card in players[i].hand:
            print(card)
           

"""
for card in players[1].hand:
    print(card)
"""
# En principio, así funciona. El único problema es que no es una solución elegante para mantener, pero por ahora va

#players[0].get_data()
#players[1].get_data()


##Ideas para solucionarlo: crear un generador que en función del número de jugadores cree una lista: [Player1, Player2, Player3...]