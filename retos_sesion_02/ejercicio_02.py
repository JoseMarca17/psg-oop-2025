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

print("\tVinos disponibles en la Vinoteca: ")
casa_real = Vino("Casa Real", "Tinto", "Tannat", 2022)
kohlberg = Vino("Kohlberg", "Rosado", "Syrah", 2021)
concepcion = Vino("La Concepción", "Blanco", "Chardonnay", 2019)
aranjuez = Vino("Aranjuez", "Tinto", "Cabernet Sauvignon", 2020)

print(f"\n{'Nombre':15} | {'Tipo':10} | {'Cepa':18} | {'Año Producción'}")
print("-" * 70)
print(f"{casa_real.nombre:15} | {casa_real.tipo:10} | {casa_real.cepa:18} | {casa_real.anio}")
print(f"{kohlberg.nombre:15} | {kohlberg.tipo:10} | {kohlberg.cepa:18} | {kohlberg.anio}")
print(f"{concepcion.nombre:15} | {concepcion.tipo:10} | {concepcion.cepa:18} | {concepcion.anio}")
print(f"{aranjuez.nombre:15} | {aranjuez.tipo:10} | {aranjuez.cepa:18} | {aranjuez.anio}")

print("\n\tQuesos disponibles en la Vinoteca:") 

san_javier = Queso("San Javier", "Criollo", 0, True)
menonita = Queso("Menonita", "Chaqueño", 1, True)
el_chaquenio = Queso("El Chaqueño", "Duro", 6, True)

print(f"\n{'Nombre':15} | {'Variedad':12} | {'Edad (meses)':12} | {'Sal':5}")
print("-" * 65)
print(f"{san_javier.nombre:15} | {san_javier.variedad:12} | {san_javier.edad:<12} | {san_javier.sal}")
print(f"{menonita.nombre:15} | {menonita.variedad:12} | {menonita.edad:<12} | {menonita.sal}")
print(f"{el_chaquenio.nombre:15} | {el_chaquenio.variedad:12} | {el_chaquenio.edad:<12} | {el_chaquenio.sal}")