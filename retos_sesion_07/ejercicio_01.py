class Martillo:
    def __init__(self, material, peso, tipo_mango):
        self._material = material
        self._peso = peso
        self._tipo_mango = tipo_mango

    def usar(self):
        print("Clavando clavos el martillo")


class Destornillador:
    def __init__(self, material, peso, tipo_mango):
        self._material = material
        self._peso = peso
        self._tipo_mango = tipo_mango

    def usar(self):
        print("Ajustando tornillos con el destornillador")


class LlaveInglesa:
    def __init__(self, material, peso, tipo_mango):
        self._material = material
        self._peso = peso
        self._tipo_mango = tipo_mango

    def usar(self):
        print("Apretando tuercas con la llave inglesa")


class Carpintero:
    def __init__(self, nombre):
        self._nombre = nombre

    def trabajar(self, herramienta):
        print(f"\n{self._nombre} está usando una herramienta")
        herramienta.usar()

martillo = Martillo("acero", 2.8, "madera")
destornillador = Destornillador("acero", 0.1, "plástico")
llave = LlaveInglesa("acero", 1 , "goma")

carpintero = Carpintero("Jose")

carpintero.trabajar(martillo)
carpintero.trabajar(destornillador)
carpintero.trabajar(llave)
