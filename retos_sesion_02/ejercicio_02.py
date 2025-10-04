class Vino:
    def __init__(self, nombre, tipo, cepa, anio):
        self.nombre = nombre 
        self.tipo = tipo
        self.cepa = cepa
        self.anio = anio

class Queso:
    def __init__(self, nombre, variedad, edad, sal):
        self.nombre = nombre
        self.variedad = variedad
        self.edad = edad
        self.sal = sal

print("\t Vinos disponibles en la Vinoteca: ")
casaReal = Vino("Casa Real", "Tinto", "Tannat", 2022)
kohlberg = Vino("Kphlberg", "Rosado", "Syrah", 2021)
concepcion = Vino("La concepcion", "Blanco", "Chardonnay", 2019)
aranjuez = Vino("Aranjuez", "Tinto", "Cabernet Sauvignon", 2020)
print(f"\n{"Nombre":15} | {"Tipo":10} | {"Cepa":18} | {"Año Producción"}")
print("-"*70)
print(f"{casaReal.nombre:15} | {casaReal.tipo:10} | {casaReal.cepa:18} | {casaReal.anio}")
print(f"{kohlberg.nombre:15} | {kohlberg.tipo:10} | {kohlberg.cepa:18} | {kohlberg.anio}")
print(f"{concepcion.nombre:15} | {concepcion.tipo:10} | {concepcion.cepa:18} | {concepcion.anio}")
print(f"{aranjuez.nombre:15} | {aranjuez.tipo:10} | {aranjuez.cepa:18} | {aranjuez.anio}")

print("\n\t Quesos disponibles en la Vinoteca:") 
sanJavier = Queso("San Javier", "Criollo", 0, True)
menonita = Queso("Menonita", "Chaqueño", 1, True)
elChaquenio = Queso("El Chaqueño", "Duro", 6, True)

print(f"\n{"Nombre":15} | {"Variedad":12} | {"Edad (meses)":12} | {"Sal":5}")
print("-"* 65)
print(f"{sanJavier.nombre:15} | {sanJavier.variedad:12} | {sanJavier.edad:<12} | {sanJavier.sal}")
print(f"{menonita.nombre:15} | {menonita.variedad:12} | {menonita.edad:<12} | {menonita.sal}")
print(f"{elChaquenio.nombre:15} | {elChaquenio.variedad:12} | {elChaquenio.edad:<12} | {elChaquenio.sal}")
