import sys
import os

sys.path.append(os.path.abspath("src"))

from service import new_register, search_record, delete_record
from file import save_data

def setup_module():
    # Datos iniciales de prueba
    save_data([])


def test_create_and_search():
    new_register("1", "Juan", "juan@gmail.com")
    result = search_record("1")
    assert result["nombre"] == "Juan"


def test_delete():
    new_register("2", "Ana", "ana@gmail.com")
    msg = delete_record("2")
    assert "eliminado" in msg.lower()