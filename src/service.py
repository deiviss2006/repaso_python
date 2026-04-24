from validate import validar_id, validar_nombre, validar_correo
from file import load_data, save_data

def new_register(id, nombre, correo):
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


def list_records():
    registros = load_data()

    if not registros:
        print("No hay registros")
        return

    for r in registros:
        print(r)

def search_record(id):
    registros = load_data()

    resultado = [r for r in registros if str(r["id"]) == str(id)]

    if not resultado:
        return "Error: ID no encontrado"

    return resultado[0]

def update_record(id, nombre=None, correo=None):
    registros = load_data()

    for r in registros:
        if str(r["id"]) == str(id):

            if nombre:
                r["nombre"] = nombre

            if correo:
                correos = {reg["correo"] for reg in registros if str(reg["id"]) != str(id)}

                try:
                    r["correo"] = validar_correo(correo, correos)
                except ValueError as e:
                    return f"Error: {e}"

                r["correo"] = correo

            save_data(registros)
            return "Registro actualizado correctamente"

    return "Error: ID no existe"

def delete_record(id):
    registros = load_data()

    nuevos = [r for r in registros if str(r["id"]) != str(id)]

    if len(nuevos) == len(registros):
        return "Error: ID no existe"

    save_data(nuevos)
    return "Registro eliminado correctamente"










