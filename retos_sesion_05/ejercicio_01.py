class Vehiculo:
    def __init__(self, velocidad, medio):
        self._velocidad = velocidad
        self._medio = medio

    @property
    def velocidad(self):
        return self._velocidad

    @property
    def medio(self):
        return self._medio

    @medio.setter
    def medio(self, nuevo_medio):
        self._medio = nuevo_medio

    def mostrar(self):
        print(f"Velocidad: {self._velocidad} km/h, Medio: {self._medio}")


class Bicicleta(Vehiculo):
    def __init__(self, velocidad, medio):
        super().__init__(velocidad, medio)

    def pedalear(self):
        self._velocidad += 2
        print("Aumentando velocidad")


class Avion(Vehiculo):
    def __init__(self, velocidad, medio):
        super().__init__(velocidad, medio)

    def volar(self):
        self._velocidad += 50
        print("Aumentando velocidad")


bici = Bicicleta(10, "terrestre")
bici.mostrar()
bici.pedalear()
print("Datos actualizados: ")
bici.mostrar()
print()
avion = Avion(150, "aereo")
avion.mostrar()
avion.volar()
print("Datos actualizados: ")
avion.mostrar()
