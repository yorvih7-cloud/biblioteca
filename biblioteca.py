# Variables globales
libreria = {
    "libro1": {
        "titulo": "1984",
        "autor": "George Orwell",
        "año_lanzamiento": 1949
    },
    "libro2": {
        "titulo": "Don Quijote",
        "autor": "Miguel de Cervantes",
        "año_lanzamiento": 1605
    },
    "libro3": {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel Garcia Marquez",
        "año_lanzamiento": 1967
    }
}

contador_id = 3

# Función para agregar libros
def agregar_libro():
    global contador_id

    # Solicita los datos
    titulo = input("Ingrese el título: ")
    autor = input("Ingrese el autor: ")
    año_lanzamiento = int(input("Ingrese el año de lanzamiento: "))

    # Valida datos obligatorios
    if not titulo or not autor:
        print("Error: El título y el autor son obligatorios.")
        return

    # Valida el año
    if año_lanzamiento < 0:
        print("Error: El año debe ser positivo.")
        return

    # Verifica libros duplicados
    for libro in libreria.values():
        if libro["titulo"].lower() == titulo.lower():
            print("Error: El libro ya existe.")
            return

    # Incrementa el contador
    contador_id += 1

    # Genera la clave
    clave = f"libro{contador_id}"

    # Guarda el libro
    libreria[clave] = {
        "titulo": titulo,
        "autor": autor,
        "año_lanzamiento": año_lanzamiento
    }

    print("Libro agregado correctamente.")

# Función para mostrar libros
def mostrar_libros():

    # Verifica si hay libros
    if len(libreria) == 0:
        print("No hay libros registrados")

    else:
        # Recorre y muestra los libros
        for clave, libro in libreria.items():
            print(f"{clave}: {libro}")

# Función para buscar libros
def buscar_libro():

    # Solicita el título
    titulo = input("Ingrese el título: ")

    # Busca coincidencias
    for libro in libreria.values():
        if libro["titulo"].lower() == titulo.lower():

            print("Libro encontrado:")
            print(libro)
            return

    # Mensaje si no existe
    print("Libro no encontrado")

# Función para eliminar libros
def eliminar_libro():

    # Solicita el título
    titulo_eliminar = input("Ingrese el título del libro a eliminar: ")

    # Busca el libro
    for clave, libro in libreria.items():
        if libro["titulo"].lower() == titulo_eliminar.lower():

            # Confirmación
            confirmar = input("¿Seguro que desea eliminar este libro? (s/n): ")

            if confirmar.lower() == "s":
                del libreria[clave]
                print("Libro eliminado correctamente.\n")

            else:
                print("Eliminación cancelada.")

            return

    # Mensaje si no encuentra el libro
    print("Libro no encontrado.\n")

# Menú principal
def menu_principal():

    while True:

        # Muestra el menú
        print("\n===== BIBLIOTECA =====")
        print("1. Registrar libro")
        print("2. Mostrar libros")
        print("3. Buscar libro")
        print("4. Eliminar libro")
        print("5. Salir")

        # Solicita una opción
        opcion = input("\nSeleccione una opción: ")

        # Navegación
        if opcion == "1":
            agregar_libro()

        elif opcion == "2":
            mostrar_libros()

        elif opcion == "3":
            buscar_libro()

        elif opcion == "4":
            eliminar_libro()

        elif opcion == "5":
            print("\nCerrando el sistema de biblioteca... ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Inicio del programa
menu_principal()

def eliminar_libro():
    titulo = input("Ingrese el título del libro a eliminar: ")

    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            biblioteca.remove(libro)
            print("Libro eliminado correctamente.")
            return

    print("Libro no encontrado.")