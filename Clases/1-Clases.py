class Persona():
    # Constructor de clase
    def __init__(self, nombre, apellido, edad): # Caracteristica compartida por todos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class Animal():
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def correr(self):
        print(f"{self.nombre} esta corriendo")

    def dormir(self):
        print(f"{self.nombre} esta durmiendo")

gatito = Animal("Chimu", "Gato")
pajaro = Animal("Lalo", "Loro")
perro = Animal("Firulais", "Perro")

print(f"El nombre del primer animal es {gatito.nombre} y es un {gatito.especie}")
print(f"El nombre del segundo animal es {pajaro.nombre} y es un {pajaro.especie}")
print(f"El nombre del tercer animal es {perro.nombre} y es un {perro.especie}")










""" Recomendacion de orden de creacion,
- Bloque de codigo
- Atributos (Estado del objeto)
- Metodos (Comportamiento)"""



