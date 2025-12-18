# Analisis

## Requisitos:
- Se debe modelar la estructura jerarquica de un edificio residencial/comercial.
- La relacion entre el Edificio y sus Pisos es de composicion, ya que un piso no tiene razon de ser sin la estructura del edificio.
- De igual forma, los Pisos tienen una relacion de composicion con Departamentos y Oficinas, pues son unidades fisicas integradas al nivel.
- El sistema debe generar identificadores automaticos basados en el numero de piso (Numeros para departamentos, Letras para oficinas).
- Se requiere una visualizacion jerarquica que muestre la direccion y nombre del edificio bajando hasta el detalle de inquilinos y telefonos.

## Objetos:
- Edificio
- Piso
- Departamento
- Oficina

## Caracteristicas:
- Edificio: 
  - nombre 
  - direccion 
  - pisos
- Piso: 
  - numero 
  - departamentos 
  - oficinas
- Departamento: 
  - numero 
  - inquilinos
- Oficina: 
  - numero 
  - telefono

## Acciones:
- Edificio: 
  - agregar_piso 
  - mostrar_informacion
- Piso: 
  - agregar_unidad 
  - mostrar_informacion
- Unidades: 
  - mostrar_informacion

## Diseño

Clases:
- Edificio:
    - Atributos: 
      - nombre
      - direccion
      - pisos 
- Piso:
    - Atributos: 
      - numero 
      - departamentos 
      - oficinas 
- Departamento:
    - Atributos: 
      - numero 
      - inquilinos 
- Oficina:
    - Atributos: 
      - numero 
      - telefono 

```mermaid
classDiagram
    class Edificio {
        +str nombre
        +str direccion
        +list pisos
        +mostrar_informacion()
    }
    class Piso {
        +int numero
        +list departamentos
        +list oficinas
        +mostrar_informacion()
    }
    class Departamento {
        +int numero
        +list inquilinos
        +mostrar_informacion()
    }
    class Oficina {
        +str numero
        +str telefono
        +mostrar_informacion()
    }
    Edificio *-- Piso
    Piso *-- Departamento
    Piso *-- Oficina