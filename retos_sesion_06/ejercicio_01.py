class Pasajero:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino

    def pasajero_informacion(self):
        print(f"Pasajero: {self.nombre}, destino: {self.destino}")


class Minibus:
    def __init__(self, numero_ruta, paradas):
        self.numero_ruta = numero_ruta
        self.paradas = paradas
        self.direccion = 1  
        self.indice_actual = 0
        self.pasajeros = []

    def parada_actual(self):
        return self.paradas[self.indice_actual]

    def avanzar(self):
        self.indice_actual += self.direccion

        if self.indice_actual >= len(self.paradas):
            self.direccion = -1
            self.indice_actual = len(self.paradas) - 2
        elif self.indice_actual < 0:
            self.direccion = 1
            self.indice_actual = 1

        print(f"Minibus {self.numero_ruta} llego a {self.parada_actual()}")
        self.bajar_pasajeros()

    def subir_pasajero(self, pasajero):
        if pasajero.destino in self.paradas:
            self.pasajeros.append(pasajero)
            print(f"{pasajero.nombre} subio al minibús con destino: {pasajero.destino}")
        else:
            print(f"{pasajero.nombre} no puede subir, su destino no está en la ruta.")

    def bajar_pasajeros(self):
        baja = [p for p in self.pasajeros if p.destino == self.parada_actual()]
        for p in baja:
            print(f"{p.nombre} bajo en {self.parada_actual()}")
            self.pasajeros.remove(p)

    def mostrar_info(self):
        print(f"\nMinibus Ruta {self.numero_ruta}")
        print(f"Recorrido: {self.paradas}")
        print(f"Parada actual: {self.parada_actual()}")
        if self.pasajeros:
            print("Pasajeros a bordo:")
            for p in self.pasajeros:
                print(f"{p.nombre} destino: {p.destino}")
        else:
            print("Sin pasajeros a bordo.")



minibus = Minibus(45, ["Arce", "Prado", "Perez"])
p1 = Pasajero("Ana", "Prado")
p2 = Pasajero("Luis", "Perez")
p3 = Pasajero("Marta", "Sopocachi")
minibus.subir_pasajero(p1)
minibus.subir_pasajero(p2)
minibus.subir_pasajero(p3)
minibus.mostrar_info()
minibus.avanzar()
minibus.mostrar_info()
minibus.avanzar()
minibus.mostrar_info()
minibus.avanzar()
