class Celula:
    def __init__(self, adn, tipo_celula, energia):
        self.__adn = adn
        self.__tipo_celula = tipo_celula
        self.__energia = energia

    @property
    def adn(self):
        return self.__adn

    @property
    def tipo_celula(self):
        return self.__tipo_celula

    @tipo_celula.setter
    def tipo_celula(self, nuevo_tipo):
        if nuevo_tipo.strip():
            self.__tipo_celula = nuevo_tipo
            print(f"Tipo de celula cambiado a: {self.__tipo_celula}")

    @property
    def energia(self):
        return self.__energia

    def comer(self):
        incremento = 20
        self.__energia += incremento
        print(f"La celula ha comido. Energia actual: {self.__energia}")

    def dividirse(self):
        if self.__energia >= 10:
            self.__energia /= 2
            print(f"Division exitosa. Energia restante: {self.__energia}")
        else:
            print("Energia insuficiente para division")

celula_estudio = Celula("ATCG", "Eucariota", 50)
print(f"ADN: {celula_estudio.adn}")
print(f"Energia inicial: {celula_estudio.energia}")

celula_estudio.comer()
celula_estudio.dividirse()
celula_estudio.tipo_celula = "Procariota"