# Análisis

## Requisitos:
- El sistema simula una batalla entre dos monstruos elegidos por dos jugadores.
- Tipos de monstruos disponibles: Dragon, Zombi, Vampiro.
- Cada monstruo es creado por una fábrica específica (Spawner).
- La batalla se realiza de la siguiente forma:
    - Dragon vence a Zombi.
    - Zombi vence a Vampiro
    - Vampiro vence a Dragon.
- Si los monstruos son iguales, es un empate.
- El juego termina cuando se ingresa "salir".

## Objetos:
- Monstruo (Dragon, Zombi, Vampiro)
- Spawner (SpawnerDragon, SpawnerZombi, SpawnerVampiro)
- Simulador 

## Características:
- Monstruo: 
  - tipo
- Dragon: 
  - tipo="Dragon"
- Zombi: 
  - tipo="Zombi"
- Vampiro: 
  - tipo="Vampiro"
- Spawner: 
  - sin características
- Simulador: 
  - sin características

## Acciones:
- Monstruo: 
  - presentarse()
- Spawner: 
  - generar()
- SpawnerDragon: 
  - generar()
- SpawnerZombi: 
  - generar()
- SpawnerVampiro: 
  - generar()
- Simulador: 
  - crear_monstruo(seleccion) 
  - determinar_ganador(m1, m2)

# Diseño

Clases:
- Monstruo:
    - Atributos:
        - tipo
    - Metodos:
        - presentarse()
- Dragon:
    - Atributos:
        - tipo = "dragon"
    - Metodos:
        - (Heredados de Monstruo)
- Zombi:
    - Atributos:
        - tipo = "zombi"
    - Metodos:
        - (Heredados de Monstruo)
- Vampiro:
    - Atributos:
        - tipo = "vampiro"
    - Metodos:
        - (Heredados de Monstruo)
- Spawner:
    - Atributos:
        - (Ninguno)
    - Metodos:
        - generar()
- SpawnerDragon:
    - Atributos:
        - (Ninguno)
    - Metodos:
        - generar() 
- SpawnerZombi:
    - Atributos:
        - (Ninguno)
    - Metodos:
        - generar() 
- SpawnerVampiro:
    - Atributos:
        - (Ninguno)
    - Metodos:
        - generar() 
- Simulador:
    - Atributos:
        - (Ninguno)
    - Metodos:
        - crear_monstruo(seleccion)
        - determinar_ganador(m1, m2)

Relaciones:
- Herencia: Dragon, Zombi y Vampiro heredan de Monstruo. Los Spawner concretos heredan de Spawner.
- Asociacion: El Simulador utiliza las clases Spawner para obtener los objetos.
- Creacion/Dependencia: Cada Spawner tiene una dependencia de creacion con su respectivo Monstruo.

## Diagrama de Clases

```mermaid
classDiagram
    class Monstruo {
        +presentarse()
    }
    class Dragon {
        +presentarse()
    }
    class Zombi {
        +presentarse()
    }
    class Vampiro {
        +presentarse()
    }
    class Spawner {
        +generar()
    }
    class SpawnerDragon {
        +generar()
    }
    class SpawnerZombi {
        +generar()
    }
    class SpawnerVampiro {
        +generar()
    }
    class Simulador {
        +crear_monstruo(seleccion)
        +determinar_ganador(m1, m2)
    }
    Monstruo <|-- Dragon
    Monstruo <|-- Zombi
    Monstruo <|-- Vampiro
    Spawner <|-- SpawnerDragon
    Spawner <|-- SpawnerZombi
    Spawner <|-- SpawnerVampiro
    Spawner --> Monstruo
    Simulador --> SpawnerS