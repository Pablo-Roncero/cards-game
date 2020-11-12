from players import Player

# Este es el archivo base del juego. Es el que se ejecutará e irá llamando al resto de archivos.

print('Welcome to "Ass Card Game" (or ACG for friends)')

# Habría que buscar una manera de evitar que el usuario introduzca valores extraños (p**** usuarios)

player_number = int(input("How many player are you?: "))

# Esta lista será usada para definir el orden del juego, aleatorizándola más adelante 
player_list = []

for i in range(player_number):
    name = input(f"Say player {i+1} name: ")
    while True:
        if name not in player_list:
            player_list.append(name)
                # Al asignar "order" aquí, asignamos el orden en el que jugaran los jugadores. Aunque si luego shuffleamos, serí irrelevante,
                # porque esos valores se sobreescribirían
            name = Player(name)
            name.get_Data()
            #print(f"Welcome {name.get_Data()}! Added to the list")
            break
        else:
            print("That name is taken... Please, choose another one")


    