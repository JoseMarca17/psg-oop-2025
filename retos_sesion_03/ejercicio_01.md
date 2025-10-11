Imagina un juego de rol en el que el personaje principal es un atleta.
Este personaje tiene tres atributos principales:

- nombre: identifica al atleta
- energía: representa su nivel de energía actual.
- fuerza: indica su capacidad física.

Cada atleta puede realizar las siguientes acciones:

- Entrenar: aumenta su fuerza, pero consume energía.
- Descansar: recupera energía.
- Comer: solo puede consumir hamburguesas, lo que también le ayuda a recuperar energí

# Análisis
## Requisitos:
- Crear un atleta.
- El atleta tiene: nombre, energía y fuerza.
- El atleta puede entrenar, descansar y comer hamburguesas.
- Entrenar aumenta fuerza, pero reduce energía.
- Descansar recupera energía.
- Comer hamburguesas también recupera energía.
- Si el atleta se queda sin energía, no puede entrenar

## Objetos
- Atleta

## Caracteristicas
- Atleta `nombre`, `energia`, `fuerza`
  
## Acciones
- Atleta: `entrenar()`, `descansar()`, `comer()`


```mermaid
classDiagram
 classDiagram
    class Atleta {
        String nombre
        float energia
        float fuerza

        entrenar()
        descansar()
        comer()
    }

```