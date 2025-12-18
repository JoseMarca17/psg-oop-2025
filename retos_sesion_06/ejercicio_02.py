class Departamento:
    def __init__(self, numero, inquilinos):
        self.numero = numero
        self.inquilinos = inquilinos

    def mostrar_info(self):
        inquilinos_str = ", ".join(self.inquilinos) if self.inquilinos else "Vacio"
        print(f"  [Dep {self.numero}] Inquilinos: {inquilinos_str}")


class Oficina:
    def __init__(self, numero, telefono):
        self.numero = numero
        self.telefono = telefono

    def mostrar_info(self):
        print(f"  [Ofi {self.numero}] Tel: {self.telefono}")


class Piso:
    def __init__(self, numero):
        self.numero = numero
        self.departamentos = []
        self.oficinas = []

    def agregar_departamento(self, unidad, inquilinos):
        numero_dep = int(f"{self.numero}{unidad:02d}")
        nuevo_dep = Departamento(numero_dep, inquilinos)
        self.departamentos.append(nuevo_dep)

    def agregar_oficina(self, letra, telefono):
        numero_ofi = f"{self.numero}{letra.upper()}"
        nueva_ofi = Oficina(numero_ofi, telefono)
        self.oficinas.append(nueva_ofi)

    def mostrar_info(self):
        print(f"\n--- Piso {self.numero} ---")
        for dep in self.departamentos:
            dep.mostrar_info()
        for ofi in self.oficinas:
            ofi.mostrar_info()


class Edificio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.pisos = []

    def construir_edificio(self, cantidad_pisos):
        for i in range(1, cantidad_pisos + 1):
            self.pisos.append(Piso(i))

    def mostrar_info(self):
        print(f"EDIFICIO: {self.nombre}")
        print(f"DIRECCION: {self.direccion}")
        for piso in self.pisos:
            piso.mostrar_info()


mi_edificio = Edificio("Mirador Andino", "Av. Arce, La Paz")
mi_edificio.construir_edificio(3)

mi_edificio.pisos[0].agregar_departamento(1, ["Andres", "Victoria"])
mi_edificio.pisos[0].agregar_oficina("A", "2123456")
mi_edificio.pisos[1].agregar_departamento(1, ["Katherin"])

mi_edificio.mostrar_info()