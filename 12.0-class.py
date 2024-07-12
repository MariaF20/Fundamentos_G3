#Herencia y poliforismo

class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return f"{self.marca} {self.modelo} esta arrancando"



class Carro(vehiculo):
    def acelerar(self):
        return f"{self.marca} {self.modelo} esta acelerando"


class Motocicleta(vehiculo):
    def caballito(self):
        return f"{self.marca} {self.modelo} esta haciendo un caballito"


carro = Carro("Toyota", "TXL")

motocicleta = Motocicleta("Pulsar", "Ns-200")

#Herende de datos
print(carro.acelerar())
print(motocicleta.caballito())

print("-----------------------------")

#Poliformismo
print(motocicleta.arrancar())
print(carro.arrancar())



