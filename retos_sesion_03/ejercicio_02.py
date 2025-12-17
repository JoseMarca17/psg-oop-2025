class Cocinero:
    total_productividad = 0
    
    recetas_permitidas = {
        "pan": {"harina", "agua"},
        "pizza": {"harina", "agua", "sal", "tomate", "queso"},
        "galleta": {"harina", "agua", "sal", "chocolate"}
    }

    def __init__(self, nombre, ingredientes_iniciales=None):
        self.nombre = nombre
        self.ingredientes = set(ingredientes_iniciales) if ingredientes_iniciales else set()
        self.productividad = 0

    def agregar_ingredientes(self, ingredientes):
        self.ingredientes.update(ingredientes)

    def preparar_receta(self, nombre_receta):
        receta = nombre_receta.lower()
        if receta in self.recetas_permitidas:
            necesarios = self.recetas_permitidas[receta]
            if necesarios.issubset(self.ingredientes):
                self.productividad += 1
                Cocinero.total_productividad += 1
                print(f"{self.nombre} preparo {receta}")
                return True
        print(f"{self.nombre} no pudo preparar {nombre_receta}")
        return False

    @classmethod
    def obtener_reporte_global(cls):
        return cls.total_productividad

chef_1 = Cocinero("Jose", ["harina", "agua", "sal"])
chef_2 = Cocinero("Andres", ["harina", "agua", "sal", "tomate", "queso"])
chef_3 = Cocinero("Alejandra", ["harina", "agua", "sal", "chocolate"])

chef_1.preparar_receta("pan")
chef_2.preparar_receta("pizza")
chef_3.preparar_receta("galleta")

print(f"Productividad agregada: {Cocinero.obtener_reporte_global()}")