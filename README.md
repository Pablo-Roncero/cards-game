# Documentación

## Descripción

Para hacer más entendible la aplicación, podemos ir escribiendo en este fichero lo que hemos conseguido hacer hasta ahora y cómo va funcionando el flujo de ejecución.

Por ahora tenemos los ficheros de card.py, card&deck.py, game.py y players.py. El fichero prueba.py, es un fichero que no contiene información relevante para la aplicación.

## Ficheros y función

El fichero central es **game.py**, que se centra en llevar a cabo el proceso de ejecución central en el juego.
Lo primero que hace es dar la bienvenida a los jugadores e importa la clase **Player** del fichero **players.py**. Tras esto, pregunta a los jugadores cuántos van a ser, define una lista vacía llamada "player_list" y mediante un bucle for, pregunta por el nombre de cada jugador. Para que no haya ningún error y que dos jugadores se puedan llamar igual en el juego, el programa va a volver a preguntar, si dicho nombre se encontrase ya guardado en "player_list", el nombre de cada participante.
Si todo va bien y el nombre no ha sido ya introducido, el jugador será bienvenido a participar en el juego. En el momento que el nombre es aceptado, este usuario será instanciado en la clase **Player** y se guardará su nombre y su rol, que por defecto será "Neutral", hasta que no se acabe la primera partida.

**QUEDA POR DESCRIBIR LA FUNCIÓN QUE TIENEN LOS FICHEROS card&deck.py y card.py**