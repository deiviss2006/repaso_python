from service import crear_registro, listar_registros
from colorama import init, Fore, Style

init(autoreset=True)

def main():
    print(Fore.CYAN + "=== SISTEMA DE REGISTROS ===")

    while True:
        print(Fore.BLUE + "\n1. Crear registro")
        print(Fore.YELLOW + "\n2. Listar registros")
        print(Fore.RED + "\n3. Salir")

        opcion = input(Fore.GREEN + "Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            correo = input("Ingrese correo: ")

            crear_registro(id, nombre, correo)

        elif opcion == "2":
            print(Fore.BLUE + "\n--- LISTA DE REGISTROS ---")
            listar_registros()

        elif opcion == "3":
            print(Fore.RED + "Saliendo del sistema...")
            break

        else:
            print(Fore.RED + "Opción inválida")

if __name__ == "__main__":
    main()