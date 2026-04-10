import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from src.app import adicionar_gasto, total_gastos, carregar_gastos


def setup_function():
    open("gastos.json", "w").write("[]")


def test_adicionar_gasto():
    adicionar_gasto(50, "comida")
    gastos = carregar_gastos()
    assert len(gastos) == 1


def test_valor_invalido():
    with pytest.raises(ValueError):
        adicionar_gasto(-10, "erro")


def test_total():
    adicionar_gasto(10, "a")
    adicionar_gasto(20, "b")
    assert total_gastos() == 30