class Jugador:
    
    jugadores_creados = 0
    posiciones_validas = {"DEL", "VOL", "DEF", "ARQ"}

    def __init__(self, nombre: str, edad: int, posicion: str):
        assert nombre.strip() != ""
        assert edad >= 15
        assert self.posicion_valida(posicion)
        self.__nombre = nombre
        self.__edad = edad
        self.__posicion = posicion
        self.goles = 0
        self.club = "Deportes Castro"
        self.energia = 100
        Jugador.jugadores_creados += 1
        assert self.club != ""
        assert 0 <= self.energia <= 100
        assert self.goles >= 0

    @classmethod
    def creados(cls):
        return cls.jugadores_creados

    @staticmethod
    def posicion_valida(posicion: str) -> bool:
        return posicion in Jugador.posiciones_validas

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        assert nueva_edad >= 15
        self.__edad = nueva_edad
        assert self.__edad >= 15

    @property
    def posicion(self):
        return self.__posicion

    def __str__(self):
        return (f"{self.__nombre} de club {self.club}, posicion: {self.__posicion}, "
                f"energia: {self.energia} con {self.goles} goles")

    def entrenar(self, minutos: int):
        assert minutos > 0
        self.energia -= minutos
        if self.energia < 0:
            self.energia = 0
        assert 0 <= self.energia <= 100

    def anotar_gol(self):
        self.goles += 1
        assert self.goles >= 0


j1 = Jugador("Pinochet", 22, "DEF")
j2 = Jugador("Piñera", 25, "DEL")

j1.club = "Deportes Castro"
j1.energia = 90
assert j1.club != ""
assert 0 <= j1.energia <= 100

j1.entrenar(10)
j1.anotar_gol()
j2.anotar_gol()

if j1.nombre < j2.nombre:
    print(j1)
    print(j2)
else:
    print(j2)
    print(j1)

print("Jugadores creados:", Jugador.creados())


    
