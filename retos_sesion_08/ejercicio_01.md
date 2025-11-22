# EJERCICIO 1
## Analisis

### Requisitos
- Debe tener dos atributos: `numerador ` y `denominador`.
- Debe poder representarse como "numerador/denominador".
- Debe poder sumar fracciones utilizando el operador +.
- Debe poder restar fracciones utilizando el operador -.
- Debe poder multiplicar fracciones utilizando el operador *.
- Debe poder dividir fracciones utilizando el operador /.
- Debe poder compararse por igualdad, menor que, mayor que y desigualdad.

### Objetos
- Fraccion

### Características
- Fraccion: numerador, denominador

### Acciones
- Fraccion: representación
- Fraccion: suma, resta, multiplicación, división
- Fraccion: igualdad, desigualdad, menor que, mayor que

```mermaid
classDiagram
    class Fraccion {
        +numerador: int
        +denominador: int
        +__str__()
        +__add__()
        +__sub__()
        +__mul__()
        +__truediv__()
        +__eq__()
        +__lt__()
        +__gt__()
        +__ne__()
    }
