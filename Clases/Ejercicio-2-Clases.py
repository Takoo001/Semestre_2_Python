class Auto:
    def __init__(self, marca: str, gasolina: float):
        self.marca = marca
        self.gasolina = gasolina
        self.kilometros_recoridos = 0  
    # METODO PARA CONDUCIR
    def conducir(self, km: int):
        # CUANTOS LITROS NECESITA
        litros_necesarios = km / 10  

        if self.gasolina >= litros_necesarios:
            # TIENE GASOLINA SUFICIENTE
            self.kilometros_recoridos += km
            self.gasolina -= litros_necesarios
            print(f"Manejaste {km} kilometros. Te quedan {self.gasolina} litros de gasolina.")
        else:
            # HASTA DONDE LLEGUE LA GASOLINA
            km_posibles = self.gasolina * 10
            self.kilometros_recoridos += km_posibles
            self.gasolina = 0
            print(f"Solo pudiste manejar {km_posibles:.0f} kilometros. Te quedaste sin gasolina.")
    # METODO PARA CARGAR GASOLINA
    def cargar_gasolina(self, litros: float):
        self.gasolina += litros
        print(f"Hechaste {litros} litros. Ahora tienes {self.gasolina} litros de gasolina.")


# DANDO LA INFORMACION QUE NECESITAN LA CLASE Y METODOS PARA FUNCIONAR ADEMAS DE LLAMARNDOLOS PARA EJECUTARSE
mi_auto = Auto("Toyota", 10)

mi_auto.conducir(50)

mi_auto.cargar_gasolina(7)