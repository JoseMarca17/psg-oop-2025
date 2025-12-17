# VINOTECA
Una vinoteca quiere registrar los vinos y quesos que ofrecen.
De cada vino se necesita registrar su nombre, tipo, cepa y 
año de producción.
De cada queso se necesita registrar su nombre, variedad, 
edad y si lleva sal.
La vinoteca tiene en su inventario 4 vinos y 3 quesos 

## Requisitos:
- Registrar los vinos
- Registrar los quesos
- Registrar los atributos de cada vino (nombre, tipo, cepa y año)
- Registrar los atributos de cada queso (nombre, variedad, edad y si lleva sal)

## Objetos:
- Vino
- Queso

## Características:
- Vino
    - nombre
    - tipo
    - cepa
    - anio

- Queso
    - nombre
    - variedad
    - edad
    - sal

## Acciones:
- (No hay acciones)

## Diseño:

Clases:
- Vino:
  - Atributos:
      - nombre 
      - tipo 
      - cepa 
      - anio 
  - Métodos:
      - (No hay acciones)

- Queso:
  - Atributos:
      - nombre 
      - variedad 
      - edad 
      - sal 
  - Métodos:
      - (No hay acciones)

## Diagrama de clases:

```mermaid
classDiagram
    class Vino {
        String nombre
        String tipo
        String cepa
        Int anio
    }
    
    class Queso {
        String nombre
        String variedad
        Int edad
        Boolean sal
    }