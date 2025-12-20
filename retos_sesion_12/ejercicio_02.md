# ANALISIS EJERCICIO 02

## Requisitos
- El sistema debe gestionar tareas individuales con título, descripción y un estado de finalización.
- Se debe permitir la creación de múltiples tareas y almacenarlas en una colección centralizada.
- El usuario debe poder eliminar tareas existentes buscando específicamente por su título.
- El sistema debe permitir marcar una tarea como completada por su título.
- Se debe listar todas las tareas registradas mostrando su estado actual.
- No se deben incluir fechas de vencimiento ni prioridades para cumplir con el principio YAGNI.
- La interacción con el usuario debe ser mediante un menú interactivo en consola.

## Objetos
- Tarea
- GestorDeTareas

## Caracteristicas
- Tarea:
  - titulo
  - descripcion
  - completada

- GestorDeTareas:
  - tareas

## Acciones
- GestorDeTareas:
  - agregar_tarea(titulo, descripcion)
  - eliminar_tarea(titulo)
  - marcar_completada(titulo)
  - listar_tareas()

## Diseño
### Clases:

- Tarea:
  - Atributos:
    - titulo
    - descripcion
    - completada
  - Metodos:
    - (no existen acciones)

- GestorDeTareas:
  - Atributos:
    - tareas
  - Metodos:
    - agregar_tarea
    - eliminar_tarea
    - marcar_completada
    - listar_tareas

## Diagrama de clases

```mermaid
classDiagram
    class Tarea {
        +titulo: string
        +descripcion: string
        +completada: bool
    }

    class GestorDeTareas {
        +tareas: list
        +agregar_tarea(titulo, descripcion)
        +eliminar_tarea(titulo)
        +marcar_completada(titulo)
        +listar_tareas()
    }

    GestorDeTareas o-- Tarea