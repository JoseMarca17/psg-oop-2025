class Monstruo:
    def __init__(self):
        self.tipo = None

    def presentarse(self):
        print(f"{self.tipo} 🧟‍♂️ listo para luchar")

class Dragon(Monstruo):
    def __init__(self):
        self.tipo = "Dragon"

class Zombi(Monstruo):
    def __init__(self):
        self.tipo = "Zombi"

class Vampiro(Monstruo):
    def __init__(self):
        self.tipo = "Vampiro"

class Spawner:
    def generar(self):
        pass

class SpawnerDragon(Spawner):
    def generar(self):
        return Dragon()

class SpawnerZombi(Spawner):
    def generar(self):
        return Zombi()

class SpawnerVampiro(Spawner):
    def generar(self):
        return Vampiro()

class Simulador:
    def crear_monstruo(self, seleccion):
        if seleccion == "dragon":
            return SpawnerDragon().generar()
        if seleccion == "zombi":
            return SpawnerZombi().generar()
        if seleccion == "vampiro":
            return SpawnerVampiro().generar()
        print("")
        return None

    def determinar_ganador(self, mounstruo_1, monstruo_2):
        if mounstruo_1.tipo == monstruo_2.tipo:
            print("Resultado: ¡Es un empate!")
            return

        reglas = {
            "Dragon": "Zombi",
            "Zombi": "Vampiro",
            "Vampiro": "Dragon"
        }

        if reglas[mounstruo_1.tipo] == monstruo_2.tipo:
            print(f"Resultado: ¡El Jugador 1 ({mounstruo_1.tipo}) gana!")
        else:
            print(f"Resultado: ¡El Jugador 2 ({monstruo_2.tipo}) gana!")

while True:
    print("-" * 30)
    print("🧩 Selección de Monstruos 🧩")
    print("Opciones: Dragon, Zombi, Vampiro")
    print('Escribe "salir" para terminar.')

    simulador = Simulador()

    seleccion_1 = input("Jugador 1: Elige tu monstruo: ").lower().strip()
    if seleccion_1 == "salir":
        print("Fin del juego. Saliendo...")
        break

    primer_monstruo = simulador.crear_monstruo(seleccion_1)
    if not primer_monstruo:
        continue
    primer_monstruo.presentarse()

    seleccion_2 = input("Jugador 2: Elige tu monstruo: ").lower().strip()
    if seleccion_2 == "salir":
        print("Fin del juego. Saliendo...")
        break

    segundo_monstruo = simulador.crear_monstruo(seleccion_2)
    if not segundo_monstruo:
        continue
    segundo_monstruo.presentarse()

    print("--- Resultado de la Batalla ---")
    simulador.determinar_ganador(primer_monstruo, segundo_monstruo)