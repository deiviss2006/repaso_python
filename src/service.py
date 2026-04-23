from validate import validar_id, validar_nombre, validar_correo
from file import load_data, save_data

def crear_registro(id, nombre, correo):
    try:
        registros = load_data()

        ids = {str(r["id"]) for r in registros}

        id_validado = validar_id(id, ids)
        nombre_validado = validar_nombre(nombre)
        correo_validado = validar_correo(correo)

        nuevo = {
            "id": id_validado,
            "nombre": nombre_validado,
            "correo": correo_validado
        }

        registros.append(nuevo)
        save_data(registros)

        print(" Registro guardado en archivo")

    except ValueError as e:
        print(f" {e}")


def listar_registros():
    registros = load_data()

    if not registros:
        print("No hay registros")
        return

    for r in registros:
        print(r)