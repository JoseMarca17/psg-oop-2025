class Instrumento:
    def __init__(self, material, peso):
        self.material = material
        self.peso = peso

    def tocar(self):
        print(f"Este instrumento es de {self.material} y {self.peso} kg")


class Guitarra(Instrumento):
    def __init__(self, material, peso, numero_cuerdas):
        super().__init__(material, peso)
        self.numero_cuerdas = numero_cuerdas

    def tocar(self):
        print(f"La guitarra de {self.numero_cuerdas} cuerdas hace: strum")


class Piano(Instrumento):
    def __init__(self, material, peso, numero_teclas):
        super().__init__(material, peso)
        self.numero_teclas = numero_teclas

    def tocar(self):
        print(f"El piano de {self.numero_teclas} teclas hace: plin")


class Tambor(Instrumento):
    def __init__(self, material, peso, tipo_percusion):
        super().__init__(material, peso)
        self.tipo_percusion = tipo_percusion

    def tocar(self):
        print(f"El tambor del tipo: {self.tipo_percusion} hace: boom")

guitarra = Guitarra("madera", 2.1, 6)
piano = Piano("madera y metal", 50.0, 88)
tambor = Tambor("fibra", 5.0, "percusión manual")

guitarra.tocar()
piano.tocar()
tambor.tocar()
