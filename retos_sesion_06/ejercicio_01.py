class Pasajero:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino

    def mostrar_informacion(self):
        print(f"Pasajero: {self.nombre} | Destino: {self.destino}")

class Minibus:
    def __init__(self, numero_ruta, paradas):
        self.numero_ruta = numero_ruta
        self.paradas = paradas
        self.indice_actual = 0
        self.direccion = 1  
        self.pasajeros = []

    def obtener_parada_actual(self):
        return self.paradas[self.indice_actual]

    def avanzar(self):
        self.indice_actual += self.direccion
        if self.indice_actual >= len(self.paradas):
            self.direccion = -1
            self.indice_actual = len(self.paradas) - 2
        elif self.indice_actual < 0:
            self.direccion = 1
            self.indice_actual = 1
            
        print(f"\nMinibus {self.numero_ruta} llego a: {self.obtener_parada_actual()}")
        self.bajar_pasajeros()

    def subir_pasajero(self, pasajero):
        if pasajero.destino in self.paradas:
            self.pasajeros.append(pasajero)
            print(f"Subio: {pasajero.nombre} (Hacia {pasajero.destino})")
        else:
            print(f"Rechazado: {pasajero.nombre} (Destino fuera de ruta)")

    def bajar_pasajeros(self):
        parada = self.obtener_parada_actual()
        a_bajar = [p for p in self.pasajeros if p.destino == parada]
        for p in a_bajar:
            print(f"Bajo: {p.nombre} en su destino {parada}")
            self.pasajeros.remove(p)

    def mostrar_informacion(self):
        print(f"--- Info Minibus {self.numero_ruta} ---")
        print(f"Parada actual: {self.obtener_parada_actual()}")
        print(f"Pasajeros a bordo: {len(self.pasajeros)}")

transporte = Minibus(45, ["Arce", "Prado", "Perez"])
p1 = Pasajero("Ana", "Prado")
p2 = Pasajero("Luis", "Perez")

transporte.subir_pasajero(p1)
transporte.subir_pasajero(p2)
transporte.avanzar()
transporte.avanzar()