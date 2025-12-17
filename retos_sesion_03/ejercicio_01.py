class Atleta:
    energia_maxima = 100

    def __init__(self, nombre, energia=100, fuerza=10):
        self.nombre = nombre
        self.energia = energia
        self.fuerza = fuerza

    def entrenar(self, horas):
        costo = horas * 20
        if self.energia >= costo:
            self.energia -= costo
            self.fuerza += horas * 5
            print(f"{self.nombre} entrenó. Fuerza: {self.fuerza}, Energía: {self.energia}")
        else:
            print(f"{self.nombre} no tiene energía suficiente para entrenar.")

    def descansar(self, horas):
        recuperacion = horas * 15
        self.energia = min(self.energia + recuperacion, self.energia_maxima)
        print(f"{self.nombre} descansó. Energía actual: {self.energia}")

    def comer(self, hamburguesas):
        
        recuperacion = hamburguesas * 10
        self.energia = min(self.energia + recuperacion, self.energia_maxima)
        print(f"{self.nombre} comió {hamburguesas} hamburguesas. Energía: {self.energia}")

    def __str__(self):
        return f"Atleta: {self.nombre} | Fuerza: {self.fuerza} | Energía: {self.energia}"

atleta_1 = Atleta("Jose", 80, 20)
atleta_2 = Atleta("Andres", 50, 15)

atleta_1.entrenar(2)
atleta_1.comer(3)
atleta_2.entrenar(3) 
atleta_2.descansar(4)

print(atleta_1)
print(atleta_2)