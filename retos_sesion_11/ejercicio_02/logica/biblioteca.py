class Biblioteca:
    def __init__(self, libros):
        self.libros = libros
        self.prestamos = {}

    def listar_libros(self):
        for indice, libro in enumerate(self.libros, start=1):
            print(f"{indice}. {libro.titulo} - {libro.autor}")

    def prestar_libro(self, usuario, indice):
        if 0 < indice <= len(self.libros):
            libro = self.libros.pop(indice - 1)
            self.prestamos.setdefault(usuario.nombre, []).append(libro)
            usuario.libros_prestados.append(libro)

    def devolver_libros(self, usuario):
        libros = self.prestamos.pop(usuario.nombre, [])
        self.libros.extend(libros)

    def mostrar_prestamos(self):
        for usuario, libros in self.prestamos.items():
            print(usuario)
            for libro in libros:
                print(libro.titulo)
