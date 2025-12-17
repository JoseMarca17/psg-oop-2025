class Animal:
    origen = "feral"  
    def __init__(self, especie, tipo, lugar_encontrado):
        self.especie = especie
        self.tipo = tipo
        self.lugar_encontrado = lugar_encontrado

print("\tAnimales que llegaron al zoológico: ")

jucumari = Animal("Jucumari", "Mamífero", "Yungas - La Paz")
jaguar = Animal("Jaguar", "Mamífero", "Rurrenabaque - Beni")
yacare = Animal("Yacaré", "Reptil", "Trinidad - Beni")
condor = Animal("Cóndor", "Ave", "Palca - La Paz")

print(f"{'Especie':15} | {'Tipo':12} | {'Origen':8} | {'Lugar encontrado'}")
print("-" * 65)
print(f"{jucumari.especie:15} | {jucumari.tipo:12} | {jucumari.origen:8} | {jucumari.lugar_encontrado}")
print(f"{jaguar.especie:15} | {jaguar.tipo:12} | {jaguar.origen:8} | {jaguar.lugar_encontrado}")
print(f"{yacare.especie:15} | {yacare.tipo:12} | {yacare.origen:8} | {yacare.lugar_encontrado}")
print(f"{condor.especie:15} | {condor.tipo:12} | {condor.origen:8} | {condor.lugar_encontrado}")