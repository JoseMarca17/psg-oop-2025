class Tarea:
    """Representa una tarea individual en el sistema."""

    def __init__(self, titulo: str, descripcion: str):
        """Inicializa una tarea.

        Args:
            titulo (str): El titulo de la tarea.
            descripcion (str): Detalle de la tarea.
        """
        self.titulo: str = titulo
        self.descripcion: str = descripcion
        self.completada: bool = False

class GestorDeTareas:
    """Clase encargada de administrar la colección de tareas."""

    def __init__(self):
        """Inicializa el gestor con una lista vacía de tareas."""
        self.tareas: list[Tarea] = []

    def agregar_tarea(self, titulo: str, descripcion: str) -> None:
        """Crea y añade una nueva tarea a la lista.

        Args:
            titulo (str): Título identificador.
            descripcion (str): Descripción del trabajo a realizar.
        """
        nueva_tarea = Tarea(titulo, descripcion)
        self.tareas.append(nueva_tarea)

    def eliminar_tarea(self, titulo: str) -> None:
        """Elimina una tarea de la lista por su título.

        Args:
            titulo (str): El título de la tarea a remover.
        """
        self.tareas = [t for t in self.tareas if t.titulo != titulo]

    def marcar_completada(self, titulo: str) -> None:
        """Busca una tarea y cambia su estado a completada.

        Args:
            titulo (str): El título de la tarea a completar.
        """
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                tarea.completada = True

    def listar_tareas(self) -> None:
        """Imprime en consola todas las tareas registradas."""
        if not self.tareas:
            print("No hay tareas registradas.")
            return
        for tarea in self.tareas:
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"[{estado}] {tarea.titulo}: {tarea.descripcion}")

def menu():
    gestor = GestorDeTareas()
    while True:
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Agregar Tarea")
        print("2. Eliminar Tarea")
        print("3. Marcar Completada")
        print("4. Listar Tareas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            t = input("Título: ")
            d = input("Descripción: ")
            gestor.agregar_tarea(t, d)
        elif opcion == "2":
            t = input("Título de la tarea a eliminar: ")
            gestor.eliminar_tarea(t)
        elif opcion == "3":
            t = input("Título de la tarea completada: ")
            gestor.marcar_completada(t)
        elif opcion == "4":
            gestor.listar_tareas()
        elif opcion == "5":
            break

if __name__ == "__main__":
    menu()