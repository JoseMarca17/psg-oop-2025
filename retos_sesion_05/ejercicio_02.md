# Analisis

## Requisitos:
- El sistema requiere un modelo de habilidades modulares para personajes de un videojuego.
- Las habilidades de nadar y volar funcionan como clases base que definen comportamientos especificos.
- Se debe aplicar herencia simple para personajes con una sola habilidad (Pez, Pajaro).
- Se requiere herencia multiple para personajes con capacidades versatiles (Pato).
- Cada personaje debe ser capaz de presentarse y declarar sus capacidades actuales de forma consolidada.

## Objetos:
- Nadador (clase padre)
- Volador (clase padre)
- Pez (clase hija)
- Pajaro (clase hija)
- Pato (clase hija )

## Caracteristicas:
- Pez: 
  - nombre_tipo
- Pajaro: 
  - nombre_tipo
- Pato: 
  - nombre_tipo

## Acciones:
- Nadador: 
  - nadar
- Volador:
  -  volar
- Pez: 
  - mostrar
- Pajaro: 
  - mostrar
- Pato: 
  - mostrar

## Diseño

Clases:
- Nadador:
    - Metodos: +nadar()
- Volador:
    - Metodos: +volar()
- Pez:
    - Metodos: +mostrar()
- Pajaro:
    - Metodos: +mostrar()
- Pato:
    - Metodos: +mostrar()

```mermaid
classDiagram
    class Nadador {
        +nadar()
    }
    class Volador {
        +volar()
    }
    class Pez {
        +mostrar()
    }
    class Pajaro {
        +mostrar()
    }
    class Pato {
        +mostrar()
    }
    Nadador <|-- Pez
    Volador <|-- Pajaro
    Nadador <|-- Pato
    Volador <|-- Pato