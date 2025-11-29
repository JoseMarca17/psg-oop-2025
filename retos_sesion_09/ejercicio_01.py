import random

class PiedraPapelTijera:
    __instancia = None
    puntaje_jugador = 0
    puntaje_computadora = 0
    opciones = ["piedra", "papel", "tijera"]

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia

    def iniciar_partida(self, eleccion):
        if eleccion not in self.opciones:
            print("Opcion invalida")
            return
        computadora = random.choice(self.opciones)
        print(f"Computadora escogio: {computadora}")
        if eleccion == computadora:
            print("Empate")
        elif (eleccion == "piedra" and computadora == "tijera") or (eleccion == "tijera" and computadora == "papel") or (eleccion == "papel" and computadora == "piedra"):
            print("Ganaste")
            self.puntaje_jugador += 1
        else:
            print("Perdiste")
            self.puntaje_computadora += 1

    def mostrar_puntaje(self):
        print(f"Jugador: {self.puntaje_jugador} | computadora: {self.puntaje_computadora}")

    def reiniciar_juego(self):
        self.puntaje_jugador = 0
        self.puntaje_computadora = 0
        print("Juego reiniciado")


juego = PiedraPapelTijera()

while True:
    print("\n------- MENU --------")
    print("1. Iniciar partida")
    print("2. Mostrar puntajes")
    print("3. Reiniciar juego")
    print("4. Salir")
    opcion = int(input("Opcion: "))

    if opcion == 1:
        eleccion = input("Elige piedra, papel o tijera: ").lower()
        juego.iniciar_partida(eleccion)
    elif opcion == 2:
        juego.mostrar_puntaje()
    elif opcion == 3:
        juego.reiniciar_juego()
    elif opcion == 4:
        break
    else:
        print("Opcion invalida")