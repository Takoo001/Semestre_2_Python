class Gato():
    def __init__(self, nombre: str, edad: int, energia: int, hambre: int):
        self.nombre = nombre
        self.edad = edad
        self.energia = energia
        self.hambre = hambre

    def distraccion(self, jugar, comida): # DE ACUERDO AL TIEMPO DE JUEGO ES LO QUE VA PERDER DE ENERGIA Y HAMBRE
        if jugar <= 15:
            juegode15 = self.energia - 10
            hambredespuesde15 = self.hambre + 15
            print(f"El gato {self.nombre} jugó durante {jugar} minutos, se canso y tiene {juegode15} de energia y {hambredespuesde15} de hambre")
        elif jugar <= 30:
            juegode30 = self.energia - 15
            hambredespuesde30 = self.hambre + 30
            print(f"El gato {self.nombre} jugó durante {jugar} minutos, se canso y tiene {juegode30} de energia y {hambredespuesde30} de hambre")
        elif jugar <= 60:
            juegode60 = self.energia - 30
            hambredespuesde60 = self.hambre + 70
            print(f"El gato {self.nombre} jugó durante {jugar} minutos, se canso y tiene {juegode60} de energia y {hambredespuesde60} de hambre")
        
        if comida in (1, 2): #EL GATO SE ESTARIA ALIMENTANDO UNICAMENTE SI JUEGA 60 MINUTOS YA QUE HAY SE CANSARIA DEMASIADO
            restauradoenergia = juegode60 + 30 
            restauradohambre = hambredespuesde60 + 30
            print(f"El gato {self.nombre} se alimento y ahora recupero energia y no tiene mucha hambre")
            print(f"Ahora tiene {restauradoenergia} de energia y {restauradohambre} de hambre")

class Espacio():
    def __init__(self, saladescanso: str, capacidadmaxima: int, lista: str):
        self.saladescanso = saladescanso
        self.capacidadmaxima = capacidadmaxima
        self.lista = []

    def agregandogato(self, nuevogato):
        nuevogato = Gato("Seba", 6, 70, 10)
        if self.capacidadmaxima < 15:
            self.capacidadmaxima + 1
        print(f"El nuevo gato a sido registrado y puesto en nuestra sala {self.saladescanso} con los siguientes datos: ")
        print(f"{nuevogato}")

Gato1 = Gato("Chimu", 2, 100, 0)
Lugar = Espacio("Descansini de gatinis", 15, ("Miguel", "Abastrubiliak", "Simbaliatikminiec"))


# CODIGO NO COMPLETADO EN EL LAB PERO PROXIMAMENTE LO HARE