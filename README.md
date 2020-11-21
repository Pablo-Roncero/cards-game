# Documentación

## Descripción

Para hacer más entendible la aplicación, podemos ir escribiendo en este fichero lo que hemos conseguido hacer hasta ahora y cómo va funcionando el flujo de ejecución.

Por ahora tenemos los ficheros de card.py, card&deck.py, game.py y players.py. El fichero prueba.py, es un fichero que no contiene información relevante para la aplicación.

## Ficheros y función

El fichero central es **game.py**, que se centra en llevar a cabo el proceso de ejecución central en el juego.
Lo primero que hace es dar la bienvenida a los jugadores e importa la clase **Player** del fichero **players.py**. Tras esto, pregunta a los jugadores cuántos van a ser, define una lista vacía llamada "player_list" y mediante un bucle for, pregunta por el nombre de cada jugador. Para que no haya ningún error y que dos jugadores se puedan llamar igual en el juego, el programa va a volver a preguntar, si dicho nombre se encontrase ya guardado en "player_list", el nombre de cada participante.
Si todo va bien y el nombre no ha sido ya introducido, el jugador será bienvenido a participar en el juego. En el momento que el nombre es aceptado, este usuario será instanciado en la clase **Player** y se guardará su nombre y su rol, que por defecto será "Neutral", hasta que no se acabe la primera partida.

En principio card&deck.py definen las clases Card y Deck. La primera crea una carta a partir del palo y el rango, los cuales hay serán parámetros a introducir, y automáticamente le asigna el valor. La seugnda, Deck, crea una baraja de cartas de manera automática: genera a partir de la clase Card tantas cartas como palos y rangos haya en las respectivas listas. Esta última clase incluye un método para mezlar la baraja, el cuál deberá ser llamado cada vez que se quiera barajar. También tiene otro método para sacar una carta de la baraja.

El fichero player.py está en proceso de desarrollo. La idea es crear un jugador y representar en esa clase todos los parámetros que se tengan que tener en cuenta para un jugador: nombre, mano, rol (culo, presi...)...

**Se han eliminado los archivos prueba.py y card.py .**

**Se plantea la idea de incluir en un único archivo todas las clases que se vayan creando, en vez de separar card&deck de players.**

## Idea

Creo que una buena idea podría ser delimitar lo que escribimos cada uno y añadir la fecha, para así saber que hemos añadido y cuándo.

## Pablo 21 Nov

Lo que he hecho principlamente es arreglar provisionalmente el problema de la asignación de variables a cada jugador. De todas formas, habría que verlo mejor, ya que sigue sin ser óptimo. También he intentado modificar la asignación de cartas a cada jugador, pero creo que hay un problema con los bucles, ya que en ese apartado hay 3, probablemente haya una manera mejor de organizarlo, porque ahora mismo se repiten cartas y no cambia de jugador para repartir las siguientes (esto no sé si podría ser problema de los cambios que he hecho yo al nombrar cada variable de los jugadores).

Dani, mira a ver si puedes ver lo del tema del reparto de cartas, porque con ese código me pierdo un poco y tú lo entiendes mejor ;) .
