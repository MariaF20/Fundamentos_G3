#Programacion Orientada a Objetos - Clases
#Manera de crear una clase

"""class Pikachu: #Clase
    pass

Pikachu_1 = Pikachu()#Objetos
Pikachu_2 = Pikachu()
Pikachu_3 = Pikachu()
Pikachu_4 = Pikachu()
"""

"""class Pikachu:
    tipo = "Electrico"

    def __init__(self):
        self.nombre = "Roco"
        self.nivel = 350
        self.salud = 800"""

    
"""
Pikachu_1 = Pikachu()"""
"""print(Pikachu_1.tipo)
print(Pikachu_1.nombre)
print(Pikachu_1.nivel)
print(Pikachu_1.salud)
"""

class Pikachu:
    tipo = "Electrico"#Variables de clase

    def __init__(self):
        self.nombre = "Roco"#Variables de Instancia
        self.nivel = 350
        self.salud = 800


Pikachu_1 = Pikachu()

#/////////////////////////////////////////////////////

class Pikachu:
    tipo = "Electrico"

    def __init__(self, nombre, nivel, sal):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = sal

    

Pikachu_2 = Pikachu("Roco", 300, 750)
Pikachu_3 = Pikachu("Buff", 700, 1200)
print(Pikachu_2.tipo, Pikachu_2.nombre, Pikachu_2.nivel, Pikachu_2.salud)
print(Pikachu_3.tipo, Pikachu_3.nombre, Pikachu_3.nivel, Pikachu_3.salud)


class Dog:
    specie = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name}, dice Woof! Woof!")

    def descripcion(self):
        return f"{self.name} tiene {self.age} años"
    
    def celebracion(self):
        return self.age + 1



dog_1 = Dog("Tony", 3)
dog_2 = Dog("Firulais", 5)


print(dog_1.specie, dog_1.name, dog_1.age)
print(dog_2.specie, dog_2.name, dog_2.age)


dog_1.bark()
dog_2.bark()

print(dog_1.descripcion())
print(dog_2.descripcion())

print(dog_1.celebracion())




