# Analisis

## Requisitos:
- Se requiere modelar la interaccion entre una unidad de transporte (Minibus) y sus usuarios (Pasajeros).
- La relacion entre Minibus y Pasajero es de agregacion, ya que los pasajeros existen de forma independiente y pueden subir o bajar del vehiculo sin afectar la existencia de este.
- El Minibus debe gestionar un recorrido circular, invirtiendo su direccion al llegar a los extremos de la lista de paradas.
- El abordaje esta condicionado a que el destino del pasajero se encuentre dentro de la ruta programada.
- El descenso es automatico cuando la ubicacion actual del minibus coincide con el destino del usuario.

## Objetos:
- Minibus
- Pasajero

## Caracteristicas:
- Minibus: 
  - numero_ruta 
  - paradas 
  - indice_actual 
  - direccion 
  - pasajeros
- Pasajero: 
  - nombre 
  - destino

Acciones:
- Minibus: 
  - avanzar 
  - subir_pasajero 
  - bajar_pasajeros 
  - mostrar_informacion
- Pasajero: 
  - mostrar_informacion

## Diseño

Clases:
- Minibus:
    - Atributos:
        - numero_ruta (int)
        - paradas (list)
        - indice_actual (int)
        - direccion (int)
        - pasajeros (list)
    - Metodos:
        - avanzar()
        - subir_pasajero(pasajero)
        - bajar_pasajeros()
        - mostrar_informacion()
- Pasajero:
    - Atributos:
        - nombre (str)
        - destino (str)
    - Metodos:
        - mostrar_informacion()

```mermaid
classDiagram
    class Minibus {
        +int numero_ruta
        +list paradas
        +int indice_actual
        +int direccion
        +list pasajeros
        +avanzar()
        +subir_pasajero(pasajero)
        +bajar_pasajeros()
        +mostrar_informacion()
    }
    class Pasajero {
        +str nombre
        +str destino
        +mostrar_informacion()
    }
    Minibus o-- Pasajero