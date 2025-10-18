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
            print(f"\nTipo de celula actualizado a: {self.__tipo_celula}")

    @property
    def energia(self):
        return self.__energia

    def comer(self, ):
        self.__energia += 20
        print("\nLa celula ha comido y ganado 20 de energía") 
        print(f"Energía actual: {self.__energia}")

    def dividirse(self):
        if self.__energia >= 2:
            self.__energia /= 2
            print("\nLa celula se ha dividido")
            print(f"Energia de la celula después de dividirse: {self.__energia}")
        else:
            print("Energía insuficiente para dividirse. La celula necesita más energía.")

celula_1 = Celula("ATCG", "Eucariota", 5)
print(f"ADN: {celula_1.adn}")
print(f"Tipo de celula: {celula_1.tipo_celula}")
print(f"Energía: {celula_1.energia}")

celula_1.tipo_celula = "Procariota"

celula_1.comer()
celula_1.dividirse()
