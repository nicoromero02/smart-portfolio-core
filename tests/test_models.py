import pytest
from src.modelos import Posicion, Instrumento

@pytest.mark.parametrize(
    "precio_entrada, precio_actual, cantidad, esperado",
    [
        (100, 150, 10, 500),   # Caso Ganancia
        (200, 180, 5, -100),   # Caso Pérdida
        (50, 50, 7, 0),        # Caso Neutral
    ],
)
def test_calculo_pnl(precio_entrada, precio_actual, cantidad, esperado, instrumento_test):
    posicion = Posicion(
        instrumento=instrumento_test,
        cantidad=cantidad,
        precio_entrada=precio_entrada
    )
    pnl = posicion.calcular_ganancia_no_realizada(precio_actual=precio_actual)
    assert pnl == pytest.approx(esperado)

# --- NUEVOS TESTS PARA MODELOS ---

def test_posicion_cantidad_negativa_lanza_error(instrumento_test):
    # Esto cubre la línea 23 de modelos.py (el setter)
    with pytest.raises(ValueError, match="La cantidad de la posición no puede ser negativa"):
        Posicion(instrumento_test, cantidad=-1, precio_entrada=100)

def test_calcular_valor_actual(instrumento_test):
    # Esto cubre la línea 27 de modelos.py
    posicion = Posicion(instrumento_test, cantidad=10, precio_entrada=100)
    assert posicion.calcular_valor_actual(precio_mercado=110) == 1100