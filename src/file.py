import json
import os

RUTA = "data/records.json"


def load_data():
    try:
        if not os.path.exists(RUTA):
            return []

        with open(RUTA, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print(" Error: archivo JSON dañado")
        return []

    except Exception as e:
        print(f" Error al leer archivo: {e}")
        return []


def save_data(data):
    try:
        with open(RUTA, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f"Error al guardar: {e}")