class Nadador:
    def nadar(self):
        print("Desplazandose por el agua...")

class Volador:
    def volar(self):
        print("Desplazandose por el aire...")

class Pez(Nadador):
    def __init__(self, nombre_tipo):
        self.nombre_tipo = nombre_tipo

    def mostrar(self):
        print(f"Tipo: {self.nombre_tipo}")
        self.nadar()

class Pajaro(Volador):
    def __init__(self, nombre_tipo):
        self.nombre_tipo = nombre_tipo

    def mostrar(self):
        print(f"Tipo: {self.nombre_tipo}")
        self.volar()

class Pato(Nadador, Volador):
    def __init__(self, nombre_tipo):
        self.nombre_tipo = nombre_tipo

    def mostrar(self):
        print(f"Tipo: {self.nombre_tipo} (Personaje Versatil)")
        self.nadar()
        self.volar()

# Implementacion
nemo = Pez("Pez Payaso")
nemo.mostrar()

zazu = Pajaro("Zanate")
zazu.mostrar()

donald = Pato("Pato")
donald.mostrar()