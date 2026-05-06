from validate import validar_id, validar_nombre, validar_correo
from file import load_data, save_data


def new_register(id: str, nombre: str, correo: str) -> str:
    """
    Crea un nuevo registro de usuario.
    """
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

        return "Registro guardado correctamente"

    except ValueError as e:
        return f"Error: {e}"


def list_records() -> list:
    """
    Retorna todos los registros.
    """
    return load_data()


def search_record(id: str) -> dict | str:
    """
    Busca un registro por ID.
    """
    registros = load_data()

    for r in registros:
        if str(r["id"]) == str(id):
            return r

    return "Error: ID no encontrado"


def update_record(id: str, nombre: str | None = None, correo: str | None = None) -> str:
    """
    Actualiza un registro existente.
    """
    registros = load_data()

    for r in registros:
        if str(r["id"]) == str(id):

            if nombre:
                try:
                    r["nombre"] = validar_nombre(nombre)
                except ValueError as e:
                    return f"Error: {e}"

            if correo:
                correos = {reg["correo"] for reg in registros if str(reg["id"]) != str(id)}

                try:
                    r["correo"] = validar_correo(correo, correos)
                except ValueError as e:
                    return f"Error: {e}"

            save_data(registros)
            return "Registro actualizado correctamente"

    return "Error: ID no existe"


def delete_record(id: str) -> str:
    """
    Elimina un registro por ID.
    """
    registros = load_data()

    nuevos = [r for r in registros if str(r["id"]) != str(id)]

    if len(nuevos) == len(registros):
        return "Error: ID no existe"

    save_data(nuevos)
    return "Registro eliminado correctamente"