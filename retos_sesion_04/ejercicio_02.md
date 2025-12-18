# Analisis

## Requisitos:
- Se requiere modelar una celula para simulaciones medicas precisas.
- El codigo genetico ADN es la base inalterable de la celula, por lo que su acceso es solo de lectura.
- El tipo de celula define su funcion y puede evolucionar o cambiar libremente.
- La energia es un recurso interno que no puede ser asignado directamente, sino que resulta de procesos biologicos como comer o dividirse.
- El proceso de division debe validar que exista suficiente energia para evitar la muerte celular.

## Objetos:
- Celula

## Caracteristicas:
- adn
- tipo_celula
- energia

## Acciones:
- comer
- dividirse
- consultar_adn
- consultar_energia
- gestionar_tipo

## Diseño

Clases:
- Celula:
    - Atributos:
        - adn 
        - tipo_celula 
        - energia 
    - Metodos:
        - comer()
        - dividirse()

```mermaid
classDiagram
    class Celula {
        - String adn
        - String tipo_celula
        - int energia
        + comer()
        + dividirse()
        + get adn()
        + get tipo_celula()
        + set tipo_celula()
        + get energia()
    }