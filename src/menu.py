from colorama import init, Fore, Style
from service import new_register, list_records, search_record, update_record, delete_record

init(autoreset=True)


def print_menu():
    print(f"\n{Fore.BLUE}{'================================='}")
    print(f"  SISTEMA DE GESTION DE USUARIOS")
    print(f"{Fore.BLUE}{'================================='}")
    print(f"  {Fore.BLUE}1. Crear registro")
    print(f"  {Fore.YELLOW}2. Listar registros")
    print(f"  {Fore.GREEN}3. Buscar registro")
    print(f"  {Fore.WHITE}4. Actualizar registro")
    print(f"  {Fore.RED}5. Eliminar registro")
    print(f"  {Fore.CYAN}6. Salir{Style.RESET_ALL}")
    print(f"{Fore.BLUE}{'-----------------------------------'}")


def run_menu():
    while True:
        print_menu()

        opcion = input(f"{Fore.GREEN}Seleccione una opcion: {Style.RESET_ALL}")

        try:
            opcion = int(opcion)
        except ValueError:
            print(f"{Fore.RED}Entrada invalida. Ingrese un numero del 1 al 6.{Style.RESET_ALL}")
            continue

        if opcion == 1:
            print(f"\n{Fore.CYAN}------ CREAR REGISTRO ------{Style.RESET_ALL}")
            id_reg = input("ID: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            new_register(id_reg, nombre, correo)
            print(f"{Fore.GREEN}Registro creado.{Style.RESET_ALL}")

        elif opcion == 2:
            print(f"\n{Fore.CYAN}------ LISTA DE REGISTROS ------{Style.RESET_ALL}")
            list_records()

        elif opcion == 3:
            print(f"\n{Fore.CYAN}------ BUSCAR REGISTRO ------{Style.RESET_ALL}")
            id_reg = input("ID a buscar: ")
            resultado = search_record(id_reg)
            print(f"{Fore.WHITE}{resultado}{Style.RESET_ALL}")

        elif opcion == 4:
            print(f"\n{Fore.CYAN}------ ACTUALIZAR REGISTRO ------{Style.RESET_ALL}")
            id_reg = input("ID a actualizar: ")
            nombre = input("Nuevo nombre (Enter para omitir): ")
            correo = input("Nuevo correo (Enter para omitir): ")
            resultado = update_record(id_reg, nombre or None, correo or None)
            print(f"{Fore.GREEN}{resultado}{Style.RESET_ALL}")

        elif opcion == 5:
            print(f"\n{Fore.CYAN}------ ELIMINAR REGISTRO ------{Style.RESET_ALL}")
            id_reg = input("ID a eliminar: ")
            resultado = delete_record(id_reg)
            print(f"{Fore.RED}{resultado}{Style.RESET_ALL}")

        elif opcion == 6:
            print(f"{Fore.GREEN}Saliendo del sistema...{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}Opcion invalida. Elija entre 1 y 6.{Style.RESET_ALL}")