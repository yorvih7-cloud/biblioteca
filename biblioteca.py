
# importaciones
from color import pintar

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
        pintar("Error: El título y el autor son obligatorios.", "rojo")
        return

    # Valida el año
    if año_lanzamiento < 0:
        pintar("Error: El año debe ser positivo.", "rojo")
        return

    # Verifica libros duplicados
    for libro in libreria.values():
        if libro["titulo"].lower() == titulo.lower():
            pintar("Error: El libro ya existe.", "rojo")
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

    pintar("Libro agregado correctamente.", "verde")

# Función para mostrar libros
def mostrar_libros():

    # Verifica si hay libros
    if len(libreria) == 0:
        pintar("No hay libros registrados", "amarillo")

    else:
        # Recorre y muestra los libros
        for clave, libro in libreria.items():
            pintar(f"{clave}: {libro}", "verde_claro")

# Función para buscar libros
def buscar_libro():

    # Solicita el título
    titulo = input("Ingrese el título: ")

    # Busca coincidencias
    for libro in libreria.values():
        if libro["titulo"].lower() == titulo.lower():

            pintar("Libro encontrado:", "verde")
            pintar(libro, "verde_claro")
            return

    # Mensaje si no existe
    pintar("Libro no encontrado", "rojo")

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
                pintar("Libro eliminado correctamente.\n", "verde")

            else:
                pintar("Eliminación cancelada.", "amarillo")

            return

    # Mensaje si no encuentra el libro
    pintar("Libro no encontrado.\n", "rojo")

#Actualizar informacion de libors

def modificar_libro():
    titulo_buscar = input("Ingresa el título del libro que deseas modificar: ")
    
    # Recorremos los libros dentro del diccionario 'libreria' de tu amigo
    for libro in libreria.values():
        if libro['titulo'].lower() == titulo_buscar.lower():
            print(f"\nLibro encontrado: {libro['titulo']} - Autor: {libro['autor']}")
            
            # Pedir los nuevos datos
            nuevo_titulo = input("Nuevo título (deja en blanco para conservar el actual): ")
            nuevo_autor = input("Nuevo autor (deja en blanco para conservar el actual): ")
            
            # Si el usuario escribió algo, se actualiza; si lo dejó en blanco, se conserva
            if nuevo_titulo.strip():
                libro['titulo'] = nuevo_titulo
            if nuevo_autor.strip():
                libro['autor'] = nuevo_autor
                
            print("¡Libro modificado con éxito!")
            return
            
    print("El libro no existe en la biblioteca.")

# Menú principal
def menu_principal():

    while True:

        # Muestra el menú
        pintar("\n===== BIBLIOTECA =====", "cian")
        pintar("1. Registrar libro", "azul")
        pintar("2. Mostrar libros", "azul")
        pintar("3. Buscar libro", "azul")
        pintar("4. Eliminar libro", "azul")
        pintar("5. Modificar libro", "azul")
        pintar("6. Salir", "azul")

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
            modificar_libro() #Nueva Funcion para modificar libros 
        
        elif opcion == "6":
            pintar("\nCerrando el sistema de biblioteca... ¡Hasta luego!", "naranja")
            break

        else:
            pintar("Opción no válida. Intente de nuevo.", "rojo")

# Inicio del programa
menu_principal()

