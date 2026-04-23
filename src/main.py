from service import crear_registro, listar_registros

def main():
    print("Sistema con persistencia\n")

    while True:
        print("\n1. Crear registro")
        print("2. Listar registros")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")

            crear_registro(id, nombre, correo)

        elif opcion == "2":
            listar_registros()

        elif opcion == "3":
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()