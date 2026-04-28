import pandas as pd
from file import load_data

def export_to_csv(filename="reporte.csv", *args, **kwargs):
    data = load_data()

    if not data:
        print("No hay datos para exportar")
        return

    df = pd.DataFrame(data)

    columnas_validas = ["id", "nombre", "correo"]

    # FILTRO
    if "filter_by" in kwargs:
        for key, value in kwargs["filter_by"].items():

            if key not in columnas_validas:
                print(f"Campo inválido: {key}")
                return

            # 👇 CONVERSIÓN IMPORTANTE
            if key == "id":
                try:
                    value = int(value)
                except ValueError:
                    print("ID inválido para filtro")
                    return

            df = df[df[key] == value]

    # VALIDAR SI QUEDÓ VACÍO
    if df.empty:
        print("No se encontraron resultados con ese filtro")
        return

    # ORDEN
    if "sort_by" in kwargs:
        if kwargs["sort_by"] in columnas_validas:
            df = df.sort_values(by=kwargs["sort_by"])
        else:
            print("Campo de orden inválido")
            return

    df.to_csv(filename, index=False)
    print(f"Reporte exportado como {filename}")