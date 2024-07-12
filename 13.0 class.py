#Encapsulamiento

"""class encap: 
    def __init__(self):
        self.__numero = 10 #Se determina que la variable es privada
    
    def operacion(self):
        print(self.__numero + 5)

    def resultado(self):
        return self.__numero

encap1 = encap()
#print(encap1.operacion())
print(encap1.resultado())
"""


### Manejo de Errores###

numero1 = 5
numero2 = 1

numero1 = "1"


#Excepcion Base
try:
    #Intenta ejecutar 
    print( numero1 + numero2)
    print("No se procede ningun error")
except:
    #Se ejecuta si hay alguna excepcion
    print("Se ha producido un error")



print("-------------------------------------")

#Flujo completo de una exprecion:
try:
    #Intenta ejecutar 
    print( numero1 + numero2)
    print("No se procede ningun error")
except:
    #Se ejecuta si hay alguna excepcion
    print("Se ha producido un error")
else:
    # Opcional Se ejecuta si no se procduce ninguna excepcion
    print("No se presenta ningun error, se sigue ejecutando de manera normal")
finally:
    #Opcional Siempre se ejecuta hayan o no hayn excepciones
    print("La ejecucion continua")

print("----------------------------")

#Excepciones por tipo de error

try:
    #Intenta ejecutar 
    print( numero1 + numero2)
    print("No se procede ningun error")
except ValueError:
    #Se ejecuta si hay alguna excepcion
    print("El error es ValueError")
except TypeError:
    #Se ejecuta si hay alguna excepcion
    print("El error es TypeError")


print("-----------------------------")

#Captura de error


try:
    #Intenta ejecutar 
    print( numero1 + numero2)
    print("No se procede ningun error")
except ValueError as error:
    print(error)
except TypeError as variable_ramdom:
    print(variable_ramdom)


print("Hola mundo")

