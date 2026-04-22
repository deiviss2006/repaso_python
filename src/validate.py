def validar_id(id, ids_existentes):
    if not id.isdigit():
        raise ValueError("El ID debe ser numérico")
    
    if id in ids_existentes:
        raise ValueError("El ID ya existe")
    
    return int(id)


def validar_nombre(nombre):
    if len(nombre.strip()) < 3:
        raise ValueError("El nombre debe tener al menos 3 caracteres")
    
    return nombre.strip()


def validar_correo(correo):
    if "@" not in correo or "." not in correo:
        raise ValueError("Correo inválido")
    
    return correo.strip()