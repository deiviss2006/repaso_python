from service import new_register, list_records, search_record, update_record, delete_record

def main():
    print("Sistema de gestion de usuarios\n")

    while True:
        print("\n1. Crear registro")
        print("2. Listar registros")
        print("3. Buscar registros")
        print("4. Actualizar registros")
        print("5. Eliminar registro")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n------ CREAR REGISTRO ------")
            id = input("ID: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")

            new_register(id, nombre, correo)

        elif opcion == "2":
            print("\n------ LISTA DE REGISTROS ------")
            list_records()

        elif opcion == "3":
            print("\n------ BUSCAR REGISTRO ------")
            id = input("Ingrese ID a buscar: ")

            resultado = search_record(id)
            print(resultado)

        elif opcion == "4":
            print("\n------ ACTUALIZAR REGISTRO ------")
            id = input("Ingrese ID a actualizar: ")
            nombre = input("Nuevo nombre (dejar vacío si no cambia): ")
            correo = input("Nuevo correo (dejar vacío si no cambia): ")

            print(update_record(id, nombre or None, correo or None))

        elif opcion == "5":
            print("\n------ ELIMINAR REGISTRO ------")
            id = input("Ingrese ID a eliminar: ")

            print(delete_record(id))

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida\n")


if __name__ == "__main__":
    main()
