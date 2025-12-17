# ZOOLOGICO
Un zoológico quiere llevar un registro de los animales que llegan 
a sus instalaciones.
Necesitan registrar su especie, tipo y lugar donde los encontraron.
Los animales del zoológico pueden ser mamíferos, reptiles o aves.
El origen de todos los animales es "feral". 
Este zoológico cuenta con 2 mamíferos, 1 reptil y 1 ave

## Requisitos:
- Registrar los animales que llegan al zoologico
- Registrar los atributos de cada animal como especie, tipo, lugar_encontrado u origen
- El origen de todos es "feral"

## Objetos:
- Animal

## Características:
- Animal
    - especie
    - tipo
    - lugar_encontrado
    - origen

## Acciones:
- (No hay acciones)

## Diseño:

Clases:
- Animal:
    - Nombre: Animal
    - Atributos:
        - especie 
        - tipo 
        - lugar_encontrado 
        - origen 
    - Métodos:
        - (No hay acciones)

## Diagrama de clases:

```mermaid
classDiagram
    class Animal {
        String especie
        String tipo
        String lugar_encontrado
        String origen
    }