class Cocinero:
    recetas_disponibles = {
        "pan": {"harina", "agua"},
        "pizza": {"harina", "agua", "sal", "tomate", "queso"},
        "galleta": {"harina", "agua", "sal", "chocolate"}
    }

    def __init__(self, nombre, ingredientes=None):
        self.nombre = nombre
        self.ingredientes = set(ingredientes) if ingredientes else set()
        self.productividad = 0

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.add(ingrediente)
        print(f"{self.nombre} agrego {ingrediente} a sus ingredientes.")

    def mostrar_ingredientes(self):
        print(f"Ingredientes de {self.nombre}: {', '.join(self.ingredientes) if self.ingredientes else 'ninguno'}")

    def preparar_receta(self, nombre_receta):
        if nombre_receta not in Cocinero.recetas_disponibles:
            print(f"La receta '{nombre_receta}' no esta en el sistema")
            return

        ingredientes_necesarios = Cocinero.recetas_disponibles[nombre_receta]
        if ingredientes_necesarios.issubset(self.ingredientes):
            self.productividad += 1
            print(f"{self.nombre} ha preparado {nombre_receta} exitosamente. Productividad: {self.productividad}")
        else:
            faltantes = ingredientes_necesarios - self.ingredientes
            print(f"{self.nombre} no puede preparar {nombre_receta}. Faltan: {', '.join(faltantes)}")

    def mostrar_productividad(self):
        print(f"Productividad de {self.nombre}: {self.productividad}")

    @staticmethod
    def calcular_productividad_total(lista_cocineros):
        total = sum(c.productividad for c in lista_cocineros)
        print(f"Productividad total de todos los cocineros: {total}")
        return total

jose = Cocinero("Jose", ["harina", "agua", "sal"])
andres = Cocinero("Andres", ["harina", "agua", "tomate", "queso", "sal"])
alejandra = Cocinero("Alejandra", ["harina", "agua", "sal", "chocolate"])

jose.mostrar_ingredientes()
andres.mostrar_ingredientes()
alejandra.mostrar_ingredientes()

jose.preparar_receta("pan")
andres.preparar_receta("pizza")
alejandra.preparar_receta("galleta")

jose.preparar_receta("galleta")

jose.mostrar_productividad()
andres.mostrar_productividad()
alejandra.mostrar_productividad()

Cocinero.calcular_productividad_total([jose, andres, alejandra])
