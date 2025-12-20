from models import ListaTareas


def main():
    lista_tareas = ListaTareas()

    while True:
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Eliminar tareas completadas")
        print("6. Eliminar todas las tareas")
        print("7. Salir")

        opcion = input()

        if opcion == "1":
            descripcion = input()
            lista_tareas.agregar_tarea(descripcion)
        elif opcion == "2":
            lista_tareas.mostrar_tareas()
        elif opcion == "3":
            lista_tareas.mostrar_tareas()
            indice = int(input())
            lista_tareas.completar_tarea(indice)
        elif opcion == "4":
            lista_tareas.mostrar_tareas()
            indice = int(input())
            lista_tareas.eliminar_tarea(indice)
        elif opcion == "5":
            lista_tareas.eliminar_completadas()
        elif opcion == "6":
            lista_tareas.eliminar_todas()
        elif opcion == "7":
            break


if __name__ == "__main__":
    main()
