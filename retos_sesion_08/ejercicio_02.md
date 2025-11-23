# Ejercicio 1
## Analisis

### Requisitos
- El catalogo debe almacenar varios destinos.
- Cada destino debe tener nombre y costo.
- El destino se representa como "[nombre] ➡ [costo] USD".
- Poder visualizar, modificar y recorrer los destinos 
- Se debe poder obtener la longitud del catalogo.
- Se debe poder acceder a los destinos por indice.
- Se debe poder asignar un destino por indice.
- Se debe poder eliminar un destino por indice.
- Se debe poder recorrer por los destinos.

### Objetos
- Destino
- Catalogo

### Características
- Destino: nombre, costo
- Catalogo: lista de destinos

### Acciones
- Destino: representación
- Catalogo: longitud, representación, acceso, asignación, eliminación, iteración

```mermaid
classDiagram
    class Destino {
        +nombre: string
        +costo: float
        +__str__()
    }

    class Catalogo {
        +destinos: List[Destino]
        +__str__()
        +__len__()
        +__getitem__()
        +__setitem__()
        +__delitem__()
        +__iter__()
    }

    Catalogo o-- Destino
