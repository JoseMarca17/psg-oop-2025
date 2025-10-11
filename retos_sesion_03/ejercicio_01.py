# Definiendo la clase
class Atleta:
    energia_maxima = 100  
    energia_minima = 0    
    
    def __init__(self, nombre, energia, fuerza):
        self.nombre = nombre
        self.energia = energia
        self.fuerza = fuerza
        self.activo = True

    @classmethod
    def crear(cls, nombre):
        print(f"El atleta {nombre} esta preparado")
        return cls(nombre, cls.energia_maxima, 10)  
    
    def entrenar(self, horas):
        if not self.activo:
            print(f"{self.nombre} ya no puede entrenar")
            return
        gasto = horas * 15
        if self.energia >= gasto:
            self.energia -= gasto
            self.fuerza += horas * 5
            print(f"{self.nombre} entrenó por {horas} hora(s)")
            print(f"Fuerza actual: {self.fuerza}" )
            print(f"Energía restante: {self.energia}")
        else:
            print(f"{self.nombre} está demasiado cansado para entrenar")
            self.verificar_estado()
    
    def descansar(self, horas):
        recuperacion = horas * 10
        self.energia = min(self.energia + recuperacion, Atleta.energia_maxima)
        print(f"{self.nombre} descansó {horas} hora(s).")
        print(f"Energía actual: {self.energia}")
    
    def comer(self, hamburguesas):
        recuperacion = hamburguesas * 20
        self.energia = min(self.energia + recuperacion, Atleta.energia_maxima)
        print(f"{self.nombre} comió {hamburguesas} hamburguesa(s)")
        print(f"Energía actual: {self.energia}")
    
    def verificar_estado(self):
        if self.energia <= Atleta.energia_minima:
            self.activo = False
            print(f"{self.nombre} esta cansado, necesita energia")
        else:
            print(f"{self.nombre} aún tiene energía")

juan = Atleta.crear("Jose")
juan.entrenar(3)
juan.comer(1)
juan.descansar(2)
juan.entrenar(5)
juan.verificar_estado()
