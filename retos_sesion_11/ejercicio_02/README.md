# ANALISIS

## Requisitos
- El sistema debe permitir registrar usuarios ingresando únicamente su nombre.
- El sistema debe contar con una lista de libros disponibles para préstamo.
- Cada libro debe tener información básica que permita identificarlo.
- El usuario debe poder ver la lista de libros antes de seleccionar alguno.
- El sistema debe permitir que un usuario preste uno o varios libros.
- Un libro prestado no debe estar disponible para otros usuarios.
- Los libros prestados deben quedar asociados al usuario correspondiente.
- La devolución de libros debe realizarse de forma conjunta.
- El sistema debe permitir ver qué libros están prestados y quién los tiene.
- El programa debe funcionar mediante interacción en consola y finalizar cuando el usuario ingrese "salir".

## Objetos

- Libro
- Usuario
- Biblioteca

## Caracteristicas

- Libro:
  - titulo
  - autor
  - isbn

- Usuario:
  - nombre
  - libros_prestados

- Biblioteca:
  - libros
  - prestamos

## Acciones

- Biblioteca:
  - listar_libros()
  - prestar_libro(usuario, indice)
  - devolver_libros(usuario)
  - mostrar_prestamos()

## Diseño
### Clases:

- Libro:
  - Atributos:
    - titulo
    - autor
    - isbn
  - Metodos:
    - (no existen acciones)

- Usuario:
  - Atributos:
    - nombre
    - libros_prestados
  - Metodos:
    - (no existen acciones)

- Biblioteca:
  - Atributos:
    - libros
    - prestamos
  - Metodos:
    - listar_libros
    - prestar_libro
    - devolver_libros
    - mostrar_prestamos

## Diagrama de clases

```mermaid
classDiagram
    class Libro {
        +titulo: string
        +autor: string
        +isbn: string
    }

    class Usuario {
        +nombre: string
        +libros_prestados: list
    }

    class Biblioteca {
        +libros: list
        +prestamos: dict
        +listar_libros()
        +prestar_libro(usuario, indice)
        +devolver_libros(usuario)
        +mostrar_prestamos()
    }

    Biblioteca o-- Libro
    Biblioteca o-- Usuario
