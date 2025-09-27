class Perro:
    especie = "canino"
    tipo = "mamífero"
    habitat = "terrestre"
    def __init__(self, nombre, edad, genero, raza, propietario):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.raza = raza
        self.propietario = propietario
chester = Perro("Toby", 6, "macho", "cocker", "Jose")
spaik = Perro("Luna", 8, "macho", "cocker", "Andres")
print("Chester: ",chester.tipo, chester.especie, chester.habitat)
print(chester.nombre)
print(chester.edad)
print(chester.genero)
print(chester.raza)
print(chester.propietario)
print("Spaik: ",spaik.tipo, spaik.especie, spaik.habitat)
print(spaik.nombre)
print(spaik.edad)
print(spaik.genero)
print(spaik.raza)
print(spaik.propietario)
print("Perro es: ", Perro.tipo, "Especie: ", Perro.especie, "Habitat: ", Perro.habitat)