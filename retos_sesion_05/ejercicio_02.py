class Nadador:
    def nadar(self):
        print("Nadando en el agua")


class Volador:
    def volar(self):
        print("Volando por el aire")


class Pez(Nadador):
    def mostrar(self):
        print("Personaje: Pez")
        self.nadar()


class Pajaro(Volador):
    def mostrar(self):
        print("Personaje: Pajaro")
        self.volar()


class Pato(Nadador, Volador):
    def mostrar(self):
        print("Personaje: Pato")
        print("Habilidades combinadas:")
        self.nadar()
        self.volar()


pez = Pez()
pez.mostrar()

pajaro = Pajaro()
pajaro.mostrar()

pato = Pato()
pato.mostrar()
