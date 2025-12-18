class Cuenta:
    def __init__(self, numero_cuenta, nombre_titular, saldo_inicial):
        self.__numero_cuenta = numero_cuenta
        self.__nombre_titular = nombre_titular
        self.__saldo = saldo_inicial

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
            print(f"Titular actualizado: {self.__nombre_titular}")
        else:
            print("Error: El nombre no puede estar vacio")

    def deposito(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Deposito exitoso. Saldo actual: {self.__saldo}")
        else:
            print("Error: El monto debe ser positivo")

    def retiro(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Saldo actual: {self.__saldo}")
        else:
            print("Error: Fondos insuficientes o monto invalido")

cuenta_persona = Cuenta("100020013290", "Jose Marca", 450.70)
print(f"Cuenta: {cuenta_persona.numero_cuenta}")
print(f"Saldo: {cuenta_persona.saldo}")

cuenta_persona.deposito(315.80)
cuenta_persona.retiro(100.00)
cuenta_persona.nombre_titular = "Rafael Gonzalo"