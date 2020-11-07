class Persona:

    def __init__(self,nombre,posicion,edad):
        self.nombre = nombre
        self.posicion = posicion
        self.edad = edad

    def tell_name(self):
        print(f"Jeg er {self.nombre}")

    def position(self):
        if self.posicion == "Manager":
            print(f"El jefe soy yo, {self.nombre}")
        else:
            print(f"Soy otro prongaillo de {self.edad} años")

pablo = Persona("Pablo","Manager","28")
dani = Persona("Dani","Ingeniero","27")

pablo.position()
print("\n")
dani.position()