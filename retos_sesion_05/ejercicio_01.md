# Analisis

## Requisitos:
- Se requiere modelar una estructura jerarquica para vehiculos de transporte.
- La velocidad es un estado critico que debe protegerse de modificaciones externas directas, permitiendo solo cambios mediante metodos internos de clase.
- El medio de desplazamiento define el entorno de operacion del vehiculo y debe ser de libre acceso.
- Los vehiculos especificos como la bicicleta y el avion deben heredar la estructura base pero implementar su propia logica de aceleracion.
- La bicicleta incrementa su velocidad por esfuerzo mecanico (pedalear).
- El avion incrementa su velocidad por propulsion (volar).

## Objetos:
- Vehiculo (clase padre)
- Bicicleta (clase hija)
- Avion (clase hija)

## Caracteristicas:
- Vehiculo: 
  - velocidad 
  - medio
- Bicicleta: 
  - (heredadas)
- Avion: 
  - (heredadas)

## Acciones:
- Vehiculo: 
  - mostrar
- Bicicleta: 
  - pedalear
- Avion: 
  - volar

## Diseño

Clases:
- Vehiculo:
    - Atributos:
        - #velocidad: int
        - +medio: str
    - Metodos:
        - +mostrar()
- Bicicleta:
    - Metodos:
        - +pedalear()
- Avion:
    - Metodos:
        - +volar()

```mermaid
classDiagram
    class Vehiculo {
        #int velocidad
        +String medio
        +mostrar()
    }
    class Bicicleta {
        +pedalear()
    }
    class Avion {
        +volar()
    }
    Vehiculo <|-- Bicicleta
    Vehiculo <|-- Avion