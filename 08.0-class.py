# 1. Listas

#De esta manera, creamos una lista
lista = [25, 26, 27, 28, 29]
         #0   1   2   2   3
         #-5 -4  -3  -2  -1 

print(lista[4])
print(lista[-2])

# de esta manera agregamos al final de la lista un valor
lista.append(5)
print(lista)


#de esta manera ingresamos aun elemento de la lista y modificamos
lista[3] = 7
print(lista)


# Eliminacion de un elemento en una lista
del lista[0]
print(lista)


#Manera de sumar los elementos
print(sum(lista))


# 2. Tuplas

#Crear una tupla
frutas = ("Manzana", "Pera", "Mango", "Kiwi")

#Manera de accecer a una tupla
print(frutas[1])
print(frutas[-1])

#Convertir una Tupla a Lista
lista_frutas = list(frutas)
print(frutas)
print(lista_frutas)


lista_frutas.append("Papaya")
print(lista_frutas)

#Convertir una Lista en tupla
print(tuple(lista_frutas))


# Diccionarios

contacto = {"Juan": "123445", #0
            "Juana": "876543", #1
            "Pedro":"5678098"} #2

#De esta manera se accede al valor asignado a la variable "Juan"
print(contacto["Juan"])

#De esta manera agregamos un valor del dic
contacto["Ana"] = "75318794"
print(contacto)


#De esta manera eliminamos un valor del dic
del contacto["Pedro"]
print(contacto)

for nombre, telefono in contacto.items():
    print(nombre, telefono)