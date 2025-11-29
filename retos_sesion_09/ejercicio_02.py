class BeatBox:
    __instancia = None
    pista = ""
    volumen = 50
    efecto = "ninguno"

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia

    def seleccionar_pista(self, nombre):
        self.pista = nombre
        print(f"Pista seleccionada: {self.pista}")

    def ajustar_volumen(self, valor):
        self.volumen += valor
        if self.volumen < 0:
            self.volumen = 0
        if self.volumen > 100:
            self.volumen = 100
        print(f"Volumen: {self.volumen}")

    def aplicar_efecto(self, efecto):
        if efecto not in ["eco", "reverb", "distorsion"]:
            print("Efecto inválido")
            return
        self.efecto = efecto
        print(f"Efecto seleccionado: {self.efecto}")

    def mostrar_estado(self):
        print(f"Pista: {self.pista} | Volumen: {self.volumen} | Efecto: {self.efecto}")


beat = BeatBox()

while True:
    print("\n ------- MENU -------")
    print("1. Ingresar pista")
    print("2. Ajustar volumen")
    print("3. Aplicar efecto")
    print("4. Mostrar estado")
    print("5. Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        pista = input("Nombre de la pista: ")
        beat.seleccionar_pista(pista)
    elif opcion == 2:
        cambio = int(input("Ingresa el volumen (+ o -)(ej. 5 o -5): "))
        beat.ajustar_volumen(cambio)
    elif opcion == 3:
        efecto = input("Elige (eco, reverb o distorsion): ").lower()
        beat.aplicar_efecto(efecto)
    elif opcion == 4:
        beat.mostrar_estado()
    elif opcion == 5:
        break
    else:
        print("Opción inválida")
