"""class Pikachu:
    tipo = "Electrico"

    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):
        self.nombre = nombre
        self.nivel = nivel
        self.__salud = salud
        self.__voltaje_max = voltaje_max
        self.amperaje_max = amperaje_max 
        self.color = color
    
    def atacar(self):
        print(f"Pikachu ataca y otorga un {self.nivel} de daño")

    def get_salud(self):
        return self.__salud
    
    def set_salud(self, salud):
        self.__salud = salud


pikachu_1 = Pikachu("Pepe", 580, 150, 6, 2, "Amarillo")



pikachu_1.set_salud(700)
print(pikachu_1.get_salud()) 
"""

class Car:
    def __init__(self, marca, modelo, velocidad_max, precio):
        self.marca = marca #Texto
        self.modelo = modelo #Texto
        self.__velocidad_max = velocidad_max #Numero, atributo privado
        self.__precio = precio #Numero, atributo privado
    
    def acelerar(self):
        self.__velocidad_max += 10
        print(f"Velocidad aumentada a {self.__velocidad_max}")

carro = Car("Mazda", "cx30", 150, 2000000)

carro.acelerar()

