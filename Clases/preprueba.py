class Membresia:
    TARIFAS_MEMBRESIAS = {"Diario": 1000, "Pase10": 9000, "Ilimitado": 20000}
    creadas = 0

    def __init__(self, nombre: str, plan: str):
        if not Membresia.es_plan_valido(plan):
            raise ValueError("Plan inválido")
        self.nombre = nombre
        self._plan = plan  
        if plan == "Diario":
            self._creditos = 1
        elif plan == "Pase10":
            self._creditos = 10
        else:  # Ilimitado
            self._creditos = float('inf') 
        self.activa = True
        Membresia.creadas += 1

    def __str__(self) -> str:
        estado = "Activa" if self.activa else "Congelada"
        creditos = "∞" if self._creditos == float('inf') else self._creditos
        return f"Membresía de {self.nombre}, Plan: {self._plan}, Créditos: {creditos}, {estado}"

    @staticmethod
    def es_plan_valido(plan: str) -> bool:
        return plan in Membresia.TARIFAS_MEMBRESIAS

    @classmethod
    def total_creadas(cls) -> int:
        return cls.creadas

    @property
    def plan(self) -> str:
        return self._plan

    @plan.setter
    def plan(self, nuevo_plan: str):
        if not self.activa:
            print("No se puede cambiar de plan: membresía congelada")
            return
        if not Membresia.es_plan_valido(nuevo_plan):
            print("Plan inválido")
            return
        self._plan = nuevo_plan
        if nuevo_plan == "Diario":
            self._creditos = 1
        elif nuevo_plan == "Pase10":
            self._creditos = 10
        else:
            self._creditos = float('inf')

    @property
    def creditos(self):
        return self._creditos

    def registrar_asistencia(self) -> bool:
        if not self.activa:
            print("Membresía congelada, no se puede registrar asistencia")
            return False
        if self._creditos == 0:
            print("No hay créditos disponibles")
            return False
        if self._creditos != float('inf'):
            self._creditos -= 1
        return True

    def congelar(self) -> None:
        """Inactiva la membresía"""
        self.activa = False

    def reactivar(self) -> None:
        """Reactiva la membresía"""
        self.activa = True

m1 = Membresia("Juan", "Diario")
print(m1) 

m1.registrar_asistencia()  
print(m1.creditos)       

m1.congelar()
print(m1)  

m1.reactivar()
m1.plan = "Pase10"
print(m1)  

print(Membresia.total_creadas()) 


# CODIGO UNICO DE ESTUDIO PARA EL LABORATORIO EN PAPEL