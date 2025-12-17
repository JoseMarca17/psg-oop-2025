# Analisis

## Requisitos:
- Crear un cocinero con inventario y recetas.
- Cada cocinero posee ingredientes y un contador de productividad.
- La productividad individual sube al preparar recetas con exito.
- La productividad de varios cocineros se suma en una metrica global.
- Solo se preparan recetas si se tienen los ingredientes necesarios.

## Objetos:
- Cocinero

## Caracteristicas:
- ingredientes
- recetas
- productividad

## Acciones:
- preparar_receta
- agregar_ingredientes
- obtener_reporte_global

## Diseño

Clases:
- Cocinero:
    - Atributos:
        - nombre
        - ingredientes
        - productividad
        - total_productividad
    - Metodos:
        - preparar_receta(nombre_receta)
        - agregar_ingredientes(ingredientes)
        - obtener_reporte_global()

```mermaid
classDiagram
    class Cocinero {
        String nombre
        set ingredientes
        int productividad
        int total_productividad
        preparar_receta(nombre_receta)
        agregar_ingredientes(ingredientes)
        obtener_reporte_global()
    }