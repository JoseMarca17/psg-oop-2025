# ANALISIS EJERCICIO 01

## Requisitos
- El sistema debe simular el lanzamiento de dos dados con valores aleatorios entre 1 y 6.
- Debe validar la victoria inmediata si la suma de los dados resulta en 7 u 11.
- Debe validar la derrota inmediata si la suma resulta en 2, 3 o 12.
- Si el resultado no es definitivo, el sistema debe permitir lanzamientos adicionales a petición del usuario.
- El flujo del juego debe terminar por victoria, derrota o cuando el jugador decida no continuar.
- Se debe evitar la implementación de registros de puntuación o nombres de usuario para cumplir con el principio YAGNI.
- El código debe incluir anotaciones de tipo y documentación clara para cada método.

## Objetos
- DadosDeLaSuerte

## Caracteristicas
- DadosDeLaSuerte:
  - (sin atributos)

## Acciones
- DadosDeLaSuerte:
  - lanzar_dados()
  - jugar()

## Diseño
### Clases:

- DadosDeLaSuerte:
  - Atributos:
    - (sin atributos)
  - Metodos:
    - lanzar_dados
    - jugar

## Diagrama de clases

```mermaid
classDiagram
    class DadosDeLaSuerte {
        +lanzar_dados() 
        +jugar() 
    }