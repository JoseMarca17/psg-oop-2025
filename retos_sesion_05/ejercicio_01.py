class Vehiculo:
    def __init__(self, velocidad, medio):
        self._velocidad = velocidad
        self.medio = medio

    def mostrar(self):
        print(f"Vehiculo en medio {self.medio} a {self._velocidad} km/h")

class Bicicleta(Vehiculo):
    def __init__(self, velocidad, medio):
        super().__init__(velocidad, medio)

    def pedalear(self):
        self._velocidad += 5
        print(f"Pedaleando... Velocidad actual: {self._velocidad} km/h")

class Avion(Vehiculo):
    def __init__(self, velocidad, medio):
        super().__init__(velocidad, medio)

    def volar(self):
        self._velocidad += 100
        print(f"Volando... Velocidad actual: {self._velocidad} km/h")

bici = Bicicleta(10, "Terrestre")
bici.mostrar()
bici.pedalear()

avion = Avion(200, "Aereo")
avion.mostrar()
avion.volar()