# Análisis

## Requisitos:
- Representar la identidad del atleta y su estado físico (fuerza y energia).
- El entrenamiento es un intercambio: se gana capacidad fisica (fuerza) a costa de vitalidad (energía).
- La recuperación de energia es vital y se logra mediante el descanso o la ingesta de un único tipo de alimento permitido (hamburguesas).
- Se debe controlar que la energia no exceda un limite maximo ni baje de un mínimo funcional.

## Objetos:
- Atleta

## Características:
- Atleta: 
  - nombre
  - energia: Valor numérico que fluctúa entre 0 y 100.
  - fuerza: Nivel de capacidad acumulado.

## Acciones:
- Atleta:
  - entrenar():
  - descansar():
  - comer(): 

## Diseño

- Clases:
- Atleta:
    - Atributos:
        - nombre 
        - energia 
        - fuerza 
    - Metodos:
        - entrenar(horas)
        - descansar(horas)
        - comer(cantidad)

```mermaid
classDiagram
    class Atleta {
        String nombre
        int energia
        int fuerza
        entrenar(horas)
        descansar(horas)
        comer(hamburguesas)
    }