"""class Persona:
    def __init__(self, nombre, edad): #Metodo clase inicializador
        self.nombre = nombre
        self.edad = edad

    def saludar(self):  #Metodo de la clase
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años")

#Instancias
persona1 = Persona("Juan", 40)
persona2 = Persona("Carla", 18)

#Llamar un metodo
persona1.saludar()
persona2.saludar()
"""

"""class calculadora:
    def __init__(self, numero):
        self.resultado = numero

    def suma(self, numero):
        self.resultado += numero

    def resta(self, numero):
        self.resultado -= numero

    def multi(self, numero):
        self.resultado *= numero

    def divi(self, numero):
        if numero != 0:
            self.resultado /= numero
        else:
            print("Error!: División por cero")


    def obt_resultado(self  ):
        return self.resultado


calculo = calculadora(0)

calculo.suma(5)
calculo.resta(4)
calculo.multi(5)
calculo.divi(2)

resOperaciones = calculo.obt_resultado()
print(resOperaciones)"""


class calculadora2:
    def suma(self, num1, num2):
        return num1 + num2

    def resta(self, num1, num2):
        return num1 - num2

    def mult(self, num1, num2):
        return num1 * num2
    
    def div(sel, num1, num2):
        if num2 == 0:
            return "No se puede dividir por cero"
        else:
            return num1 / num2

calculadora = calculadora2()

numero1 = float(input("Ingrese numero1: "))
numero2 = float(input("Ingrese numero2: "))

print(calculadora.suma(numero1, numero2))
print(calculadora.resta(numero1, numero2))
print(calculadora.mult(numero1, numero2))
print(calculadora.div(numero1, numero2))