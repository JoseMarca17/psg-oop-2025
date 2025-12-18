# Analisis

## Requisitos:
- Un banco necesita un sistema para administrar cuentas de forma segura.
- Los datos criticos como el saldo y el numero de cuenta deben ser protegidos para evitar manipulaciones externas.
- El saldo solo puede alterarse mediante procesos validados de deposito y retiro.
- El numero de cuenta es una identidad fija que no debe cambiar tras su creacion.
- La identidad del titular es flexible y puede actualizarse segun se requiera.

## Objetos:
- Cuenta

## Caracteristicas:
- numero_cuenta
- nombre_titular
- saldo

## Acciones:
- deposito
- retiro
- consultar_saldo
- consultar_numero_cuenta
- modificar_titular

## Diseño

Clases:
- Cuenta:
    - Atributos:
        - numero_cuenta 
        - nombre_titular 
        - saldo 
    - Metodos:
        - deposito(monto)
        - retiro(monto)

```mermaid
classDiagram
    class Cuenta {
        - String numero_cuenta
        + String nombre_titular
        - float saldo
        + deposito(monto)
        + retiro(monto)
        + get numero_cuenta()
        + get saldo()
        + get nombre_titular()
        + set nombre_titular()
    }