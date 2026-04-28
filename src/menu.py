from colorama import init, Fore, Style
from service import new_register, list_records, search_record, update_record, delete_record
from integration import export_to_csv

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
    print(f"  {Fore.MAGENTA}6. Exportar a CSV")
    print(f"  {Fore.CYAN}7. Salir{Style.RESET_ALL}")
    print(f"{Fore.BLUE}{'-----------------------------------'}")


def run_menu():
    while True:
        print_menu()

        opcion = input(f"{Fore.GREEN}Seleccione una opcion: {Style.RESET_ALL}")

        try:
            opcion = int(opcion)
        except ValueError:
            print(f"{Fore.RED}Entrada invalida. Ingrese un numero del 1 al 7.{Style.RESET_ALL}")
            continue

        if opcion == 1:
            print(f"\n{Fore.CYAN}------ CREAR REGISTRO ------{Style.RESET_ALL}")
            id_reg = input("ID: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")

            resultado = new_register(id_reg, nombre, correo)

            if resultado and "Error" in resultado:
                print(Fore.RED + resultado)
            else:
                print(Fore.GREEN + (resultado or "Registro creado correctamente"))

        elif opcion == 2:
            print(f"\n{Fore.CYAN}------ LISTA DE REGISTROS ------{Style.RESET_ALL}")
            list_records()

        elif opcion == 3:
            print(f"\n{Fore.CYAN}------ BUSCAR REGISTRO ------{Style.RESET_ALL}")
            id_reg = input("ID a buscar: ")
            resultado = search_record(id_reg)

            if isinstance(resultado, str) and "Error" in resultado:
                print(Fore.RED + resultado)
            else:
                print(Fore.WHITE + str(resultado))

        elif opcion == 4:
            print(f"\n{Fore.CYAN}------ ACTUALIZAR REGISTRO ------{Style.RESET_ALL}")
            id_reg = input("ID a actualizar: ")
            nombre = input("Nuevo nombre (Enter para omitir): ")
            correo = input("Nuevo correo (Enter para omitir): ")

            resultado = update_record(id_reg, nombre or None, correo or None)

            if "Error" in resultado:
                print(Fore.RED + resultado)
            else:
                print(Fore.GREEN + resultado)

        elif opcion == 5:
            print(f"\n{Fore.CYAN}------ ELIMINAR REGISTRO ------{Style.RESET_ALL}")
            id_reg = input("ID a eliminar: ")

            confirm = input("¿Seguro que deseas eliminar? (s/n): ").lower()
            if confirm != "s":
                print(Fore.YELLOW + "Operacion cancelada")
                continue

            resultado = delete_record(id_reg)

            if "Error" in resultado:
                print(Fore.RED + resultado)
            else:
                print(Fore.GREEN + resultado)

        elif opcion == 6:
            print(f"\n{Fore.CYAN}------ EXPORTAR REPORTE ------{Style.RESET_ALL}")

            campo = input("Ordenar por (id/nombre/correo o Enter): ")
            filtro_campo = input("Filtrar campo (id/nombre/correo o Enter): ")
            filtro_valor = input("Valor del filtro: ")

            kwargs = {}

            if campo:
                kwargs["sort_by"] = campo

            if filtro_campo and filtro_valor:
                kwargs["filter_by"] = {filtro_campo: filtro_valor}

            export_to_csv(**kwargs)

        elif opcion == 7:
            print(f"{Fore.GREEN}Saliendo del sistema...{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}Opcion invalida. Elija entre 1 y 7.{Style.RESET_ALL}")