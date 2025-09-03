class Persona():
    def __init__(self, nombre: str, edad: int, altura: float, peso: float):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura  
        self.peso = peso         
    
        
    # Para calcular IMC
    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        print(f"El IMC de {self.nombre} es: {imc:.2f}")
        
        if imc < 18.5:
            print("Estado: Bajo peso")
        elif 18.5 <= imc < 25:
            print("Estado: Peso normal")
        elif 25 <= imc < 30:
            print("Estado: Sobrepeso")
        else:
            print("Estado: Obesidad")
        return imc        
        
        
    # Para sacar promedio de asignatura
    def promedio_asignatura(self, nota1: float, nota2: float, nota3: float):
        promedio = (nota1 + nota2 + nota3) / 3
        print(f"Promedio de {self.nombre}: {promedio:.2f}")
        
        if promedio >= 4.0:
            print("Estas aprobado")
        else:
            print("Estas repobrado")
        return promedio


# Datos de la persona (Guardado como persona1)
persona1 = Persona("Matías", 20, 1.75, 74)

# Calculando IMC
persona1.calcular_imc()

# Promeido asignatura
persona1.promedio_asignatura(4.5, 3.8, 4.2)
