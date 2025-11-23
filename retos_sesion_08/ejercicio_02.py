class Destino:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = float(costo)

    def __str__(self):
        return f"[{self.nombre} ➡ {self.costo} USD]"


class Catalogo:
    def __init__(self):
        self.destinos = []

    def __str__(self):
        texto = "🗺 Destinos 🗺\n"
        indice = 1
        for destino in self.destinos:
            texto += f"{indice}. {destino}\n"
            indice += 1
        return texto.strip()

    def __len__(self):
        return len(self.destinos)

    def __getitem__(self, indice):
        return self.destinos[indice]

    def __setitem__(self, indice, valor):
        self.destinos[indice] = valor

    def __delitem__(self, indice):
        del self.destinos[indice]

    def __iter__(self):
        return iter(self.destinos)

catalogo = Catalogo()

catalogo.destinos.append(Destino("Cairo", 1200))
catalogo.destinos.append(Destino("Milan", 1300))
catalogo.destinos.append(Destino("Madrid", 900))
catalogo.destinos.append(Destino("Bogota", 300))

print(catalogo)
print("Longitud:", len(catalogo))
print("Primer destino:", catalogo[0])

catalogo[2] = Destino("Monterrey", 1000)
del catalogo[1]

print("\nCatalogo actualizado:")
print(catalogo)
