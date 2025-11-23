# EJERCICIO 1
## Analisis
### Requisitos
- Cada fraccion debe tener dos atributos: `numerador ` y `denominador`.
- La fraccion debe poder representarse como "numerador/denominador".
- Se debe sumar fracciones utilizando el operador +.
- Se debe restar fracciones utilizando el operador -.
- Se debe multiplicar fracciones utilizando el operador *.
- Se debe dividir fracciones utilizando el operador /.
- Se debe porder comparar las fracciones por igualdad, menor que, mayor que y desigualdad.

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
