from .tarea import Tarea


class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        self.tareas.append(Tarea(descripcion))

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas.")
            return

        for indice, tarea in enumerate(self.tareas, start=1):
            estado = "X" if tarea.completada else " "
            print(f"{indice}. [{estado}] {tarea.descripcion}")

    def completar_tarea(self, indice):
        if 0 < indice <= len(self.tareas):
            self.tareas[indice - 1].marcar_completada()

    def eliminar_tarea(self, indice):
        if 0 < indice <= len(self.tareas):
            self.tareas.pop(indice - 1)

    def eliminar_completadas(self):
        self.tareas = [tarea for tarea in self.tareas if not tarea.completada]

    def eliminar_todas(self):
        self.tareas.clear()
