from modelos import Libro, Usuario
from logica import Biblioteca


def main():
    libros = [
        Libro("Harry Potter y el cáliz de fuego", "J. K. Rowling", "9780439139601"),
        Libro("Misery", "Stephen King", "9780450417399"),
        Libro("La vuelta al mundo en ochenta días", "Julio Verne", "9780451530530"),
    ]

    biblioteca = Biblioteca(libros)

    while True:
        nombre = input("Ingrese su nombre o 'salir' para salir del programa: ")
        if nombre.lower() == "salir":
            break

        usuario = Usuario(nombre)

        while True:
            print("\nLibros disponibles:")
            biblioteca.listar_libros()
            print("\nOpciones:")
            print("1. Prestar libro")
            print("2. Ver mis libros")
            print("3. Devolver libros")
            print("4. Ver todos los préstamos")
            print("Escriba 'salir' para volver al menú principal")

            opcion = input("Seleccione una opcion: ").lower()
            if opcion == "salir":
                break

            elif opcion == "1":
                while True:
                    indice = input("Seleccione el número del libro a prestar o 'salir' para volver: ")
                    if indice.lower() == "salir":
                        break
                    if indice.isdigit():
                        biblioteca.prestar_libro(usuario, int(indice))
                        print(f"Libro prestado correctamente a {usuario.nombre}")
                    else:
                        print("Opción inválida. Intente de nuevo.")

            elif opcion == "2":
                if not usuario.libros_prestados:
                    print("No tiene libros prestados")
                else:
                    print("Mis libros prestados:")
                    for libro in usuario.libros_prestados:
                        print(f"- {libro.titulo}")

            elif opcion == "3":
                if usuario.libros_prestados:
                    biblioteca.devolver_libros(usuario)
                    print("Todos los libros fueron devueltos correctamente")
                else:
                    print("No tiene libros para devolver")

            elif opcion == "4":
                print("\nLibros prestados actualmente:")
                biblioteca.mostrar_prestamos()

            else:
                print("Opción inválida. Intente nuevamente.")

    print("Saliendo del programa ...")


if __name__ == "__main__":
    main()
