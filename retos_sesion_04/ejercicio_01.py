class Cuenta:
    def __init__(self, numero_cuenta, nombre_titular,saldo):
        self.__numero_cuenta = numero_cuenta
        self.nombre_titular = nombre_titular
        self.__saldo = saldo
        
    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def saldo(self):
        return self.__saldo

    @property
    def nombre_titular(self):
        return self.__nombre_titular

    @nombre_titular.setter
    def nombre_titular(self, nuevo_nombre):
        if nuevo_nombre.strip():
            self.__nombre_titular = nuevo_nombre
            print(f"\nNombre del titular actualizado a: {nuevo_nombre}")
        else:
            print("Error: Debe introducir un nombre")

    def deposito(self, monto) :
        if monto > 0:
            self.__saldo += monto
            print("\nDeposito exitoso :)")
            print("Monto depositado: ", monto)
            print("Saldo actual: ", self.__saldo)
        else:
            print("\nError: el monto del depósito debe ser positivo.")

    def retiro(self, monto):
        if monto <= 0:
            print("\nError: el monto del retiro debe ser positivo.")
        elif monto > self.__saldo:
            print("\nSaldo insuficiente :( No se pudo realizar el retiro.")
        else:
            self.__saldo -= monto
            print("\nRetiro exitoso :)")
            print("Monto retirado: ", monto)
            print("Saldo actual: ", self.__saldo)

cuenta_1 = Cuenta(100020013290,"Jose Marca", 450.70)
print(f"Número de cuenta: {cuenta_1.numero_cuenta}")
print(f"Titular: {cuenta_1.nombre_titular}")
print(f"Saldo inicial: {cuenta_1.saldo}")

cuenta_1.deposito(315.80)
cuenta_1.retiro(567.30)
cuenta_1.retiro(600)

cuenta_1.nombre_titular = "Rafael Gonzalo"