from validate import validar_id, validar_nombre, validar_correo

# Estructuras en memoria
registros = []
ids = set()


def crear_registro(id, nombre, correo):
    try:
        id_validado = validar_id(id, ids)
        nombre_validado = validar_nombre(nombre)
        correo_validado = validar_correo(correo)

        registro = {
            "id": id_validado,
            "nombre": nombre_validado,
            "correo": correo_validado
        }

        registros.append(registro)
        ids.add(id)

        print("Registro creado correctamente")

    except ValueError as e:
        print(f"Error: {e}")


def listar_registros():
    if not registros:
        print("No hay registros")
        return

    for r in registros:
        print(r)