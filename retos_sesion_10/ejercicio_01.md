# Análisis

## Requisitos:
- La heladeria ofrece dos sabores: Vainilla y Chocolate.
- El cliente elige el sabor y el tipo de envase (Cono o Vaso) mediante un menu
- Existen maquinas especializadas: una para Vainilla y otra para Chocolate.
- Todos los helados deben poderse comer y tienen un envase definido al crearse.
- Si se ingresa "salir", el programa termina.

## Objetos:
- Helado (Vainilla, Chocolate)
- Maquina (MaquinaVainilla, MaquinaChocolate)
- Heladero 

## Características:
- Helado: 
  - envase
- HeladoVainilla: (Helado)
- HeladoChocolate: (Helado)
- Maquina: 
  - sin características
- MaquinaVainilla: (Maquina)
- MaquinaChocolate: (Maquina)
- Heladero: 
  - sin características

Acciones:
- Helado: 
  - comer()
- HeladoVainilla: 
  - comer()
- HeladoChocolate: 
  - comer()
- Maquina: 
  - preparar(envase)
- MaquinaVainilla: 
  - preparar(envase)
- MaquinaChocolate: 
  - preparar(envase)
- Heladero: 
  - tomar_pedido(opcion)

## Diseño

Clases:
- Helado:
    - Atributos:
        - envase
    - Metodos:
        - comer()
- HeladoVainilla:
    - Atributos:
        - (Heredados de Helado)
    - Metodos:
        - comer() 
- HeladoChocolate:
    - Atributos:
        - (Heredados de Helado)
    - Metodos:
        - comer() 
- Maquina:
    - Atributos:
        - (Ninguno)
    - Metodos:
        - preparar(envase)
- MaquinaVainilla:
    - Atributos:
        - (Ninguno)
    - Metodos:
        - preparar(envase) 
- MaquinaChocolate:
    - Atributos:
        - (Ninguno)
    - Metodos:
        - preparar(envase) 
- Heladero:
    - Atributos:
        - (Ninguno)
    - Metodos:
        - tomar_pedido(opcion)

Relaciones:
- Herencia: HeladoVainilla y HeladoChocolate heredan de Helado. MaquinaVainilla y MaquinaChocolate heredan de Maquina.
- Asociacion: El Heladero utiliza a las subclases de Maquina para procesar pedidos.

# Diagrama de Clases

```mermaid
classDiagram
    class Helado {
        +comer()
    }
    class HeladoVainilla {
        +comer()
    }
    class HeladoChocolate {
        +comer()
    }
    class Maquina {
        +preparar(envase)
    }
    class MaquinaVainilla {
        +preparar(envase)
    }
    class MaquinaChocolate {
        +preparar(envase)
    }
    class Heladero {
        +tomar_pedido(opcion)
    }
    Helado <|-- HeladoVainilla
    Helado <|-- HeladoChocolate
    Maquina <|-- MaquinaVainilla
    Maquina <|-- MaquinaChocolate
    Maquina --> Helado
    Heladero --> Maquina