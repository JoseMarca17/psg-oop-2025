class Departamento:
    def __init__(self, numero, inquilinos):
        self.numero = numero
        self.inquilinos = inquilinos

    def mostrar_info(self):
        print(f"Departamento {self.numero}")
        if self.inquilinos:
            print("   Inquilinos:")
            for i in self.inquilinos:
                print(f" {i} ")
        else:
            print(" (Sin inquilinos)")


class Oficina:
    def __init__(self, numero, telefono):
        self.numero = numero
        self.telefono = telefono

    def mostrar_info(self):
        print(f"Oficina {self.numero} | Telefono: {self.telefono}")


class Piso:
    def __init__(self, numero):
        self.numero = numero
        self.departamentos = []
        self.oficinas = []

    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)
        print(f"Departamento {departamento.numero} agregado al piso {self.numero}")

    def agregar_oficina(self, oficina):
        self.oficinas.append(oficina)
        print(f"Oficina {oficina.numero} agregada al piso {self.numero}")

    def mostrar_info(self):
        print(f"\nPiso {self.numero}")
        if self.departamentos:
            print("Departamentos:")
            for dep in self.departamentos:
                dep.mostrar_info()
        else:
            print("No hay departamentos.")

        if self.oficinas:
            print("\nOficinas:")
            for ofi in self.oficinas:
                ofi.mostrar_info()
        else:
            print("No hay oficinas.")


class Edificio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.pisos = []

    def agregar_piso(self, piso):
        self.pisos.append(piso)
        print(f"Piso {piso.numero} agregado al edificio '{self.nombre}'")

    def mostrar_info(self):
        print(f"\nEdificio: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print("=" * 40)
        for piso in self.pisos:
            piso.mostrar_info()
        print("=" * 40)
        print("Fin de información del edificio.")

edificio = Edificio("Mirador Andino", "Av. Arce #1234, La Paz")
piso1 = Piso(1)
piso2 = Piso(2)
piso3 = Piso(3)
piso1.agregar_departamento(Departamento(101, ["Andres", "Victoria"]))
piso1.agregar_oficina(Oficina("1A", "2123456"))
piso2.agregar_departamento(Departamento(201, ["Katherin"]))
piso2.agregar_departamento(Departamento(202, ["José", "Elena"]))
piso2.agregar_oficina(Oficina("2B", "2334455"))
piso3.agregar_oficina(Oficina("3A", "2456789"))
piso3.agregar_oficina(Oficina("3C", "2456799"))
edificio.agregar_piso(piso1)
edificio.agregar_piso(piso2)
edificio.agregar_piso(piso3)
edificio.mostrar_info()
