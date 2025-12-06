class Helado:
    def __init__(self, envase):
        self.envase = envase

    def comer(self):
        print(f"Helado 🍦 en {self.envase}")

class HeladoVainilla(Helado):
    def comer(self):
        print(f"Vainilla 🍦 en {self.envase}")

class HeladoChocolate(Helado):
    def comer(self):
        print(f"Chocolate 🍦 en {self.envase}")

class Maquina:
    def preparar(self, envase):
        pass

class MaquinaVainilla(Maquina):
    def preparar(self, envase):
        return HeladoVainilla(envase)

class MaquinaChocolate(Maquina):
    def preparar(self, envase):
        return HeladoChocolate(envase)

class Heladero:
    def tomar_pedido(self, opcion):
        if opcion == "1":
            return MaquinaVainilla().preparar("Cono")
        if opcion == "2":
            return MaquinaVainilla().preparar("Vaso")
        if opcion == "3":
            return MaquinaChocolate().preparar("Cono")
        if opcion == "4":
            return MaquinaChocolate().preparar("Vaso")
        print("Opcion invalida. Intente nuevamente ....")
        return None

while True:
    print("\n🍨 Pedidos de Helado 🍨")
    print("1. Vainilla en Cono")
    print("2. Vainilla en Vaso")
    print("3. Chocolate en Cono")
    print("4. Chocolate en Vaso")
    print('Escribe "salir" para terminar.')

    opcion = input("Elige una opción: ").lower().strip()

    if opcion == "salir":
        print("Saliendo ....")
        break

    heladero = Heladero()
    helado = heladero.tomar_pedido(opcion)

    if helado:
        helado.comer()