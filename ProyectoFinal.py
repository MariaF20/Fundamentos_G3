class Libro:
    def __init__(self, titulo, autor, genero, año):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año = año
        self.prestado = False

    def prestar(self):
        self.prestado = True

    def devolver(self):
        self.prestado = False

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"{self.titulo} de {self.autor}, Género: {self.genero}, Año: {self.año}, Estado: {estado}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, titulo):
        self.libros = [libro for libro in self.libros if libro.titulo != titulo]
        """self.libros = []
        for libro in self.libros:
            if libro != libro.titulo:
                self.libro.append(libro)"""

    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros if libro.titulo == titulo]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros if libro.autor == autor]

    def buscar_por_genero(self, genero):
        return [libro for libro in self.libros if libro.genero == genero]

    def listar_libros(self):
        return self.libros



# Ejemplo de uso
biblioteca = Biblioteca()


# Interfaz de usuario simple
def menu():
    print("\nSistema de Gestión de Biblioteca")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Buscar libro por título")
    print("4. Buscar libro por autor")
    print("5. Buscar libro por género")
    print("6. Listar todos los libros")
    print("7. Prestar libro")
    print("8. Devolver libro")
    print("9. Guardar y salir")

while True:
    menu()
    opcion = input("\nSeleccione una opcion: ")

    if opcion == "1":
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        genero = input("Genero: ")
        año = input("Año: ")
        libro = Libro(titulo, autor, genero, año)
        biblioteca.agregar_libro(libro)
    
    elif opcion == "2":
        titulo = input("Titulo del libro a eliminar es: ")
        biblioteca.eliminar_libro(titulo)
    
    elif opcion == "3":
        titulo = input ("Titulo del libro a buscar es: ")
        busqueda = biblioteca.buscar_por_titulo(titulo)
        for libro in busqueda:
            print(libro)

    elif opcion == "4":
        autor = input ("Autor del libro a buscar es: ")
        busqueda = biblioteca.buscar_por_autor(autor)
        for libro in busqueda:
            print(libro)

    elif opcion == "5":
        genero = input ("Genero del libro a buscar es: ")
        busqueda = biblioteca.buscar_por_genero(genero)
        for libro in busqueda:
            print(libro)

    elif opcion == "6":
        for libro in biblioteca.listar_libros():
            print(libro)

    elif opcion == "7":
        titulo = input ("Titulo del libro a prestar es: ")
        resultado = biblioteca.buscar_por_titulo(titulo)
        if resultado:
            resultado [0].prestar()
            print (f"El libro '{titulo}', ha sido prestado")
        else: 
            print("Libro no encontrado")
    
    elif opcion == "8":
        titulo = input ("Titulo del libro a devolver es: ")
        resultado = biblioteca.buscar_por_titulo(titulo)
        if resultado:
            resultado [0].devolver()
            print (f"El libro '{titulo}', ha sido devuelto")
        else: 
            print("Libro no encontrado")

    
    
    elif opcion == "9":
        print("Datos guardados, saliendo del sistema.")
        break
    
    else: 
        print("Opcion no Valida, intente nuevamente!")
    


        
    
