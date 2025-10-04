class Animal:
    origen = "feral"
    def __init__(self, especie, tipo, lugarEncontrado):
        self.especie = especie
        self.tipo = tipo
        self.lugarEncontrado = lugarEncontrado

print("\tAnimales que llegaron al zoologico: ")

jucumari = Animal("Jucumari", "Mamifero", "Yungas - La Paz ")
jaguar = Animal("Jaguar", "Mamifero", "Rurrenabaque - Beni")
yacare = Animal("Yacare", "Reptil","Trinidad - Beni")
condor = Animal("Condor","Ave","Palca - La Paz")

print(f"{"Especie":15} | {"Tipo":12} | {"Origen":8} | {"Lugar encontrado"}")
print("-"*65)
print(f"{jucumari.especie:15} | {jucumari.tipo:12} | {jucumari.origen:8} | {jucumari.lugarEncontrado}")
print(f"{jaguar.especie:15} | {jaguar.tipo:12} | {jaguar.origen:8} | {jaguar.lugarEncontrado}")
print(f"{yacare.especie:15} | {yacare.tipo:12} | {yacare.origen:8} | {yacare.lugarEncontrado}")
print(f"{condor.especie:15} | {condor.tipo:12} | {condor.origen:8} | {condor.lugarEncontrado}")
