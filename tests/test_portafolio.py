import pytest
from src.portafolio import Portafolio, PosicionNoExisteError
from src.modelos import Posicion

def test_remover_activo_inexistente_lanza_error(portafolio_vacio):
    with pytest.raises(PosicionNoExisteError):
        portafolio_vacio.remover_posicion(ticker="MSFT")

# --- NUEVOS TESTS PARA PORTAFOLIO ---

def test_agregar_posicion_tipo_incorrecto(portafolio_vacio):
    # Esto cubre las líneas 14-15 de portafolio.py
    with pytest.raises(TypeError, match="Solo se pueden agregar objetos de tipo Posicion"):
        portafolio_vacio.agregar_posicion("No soy una posicion")

def test_acceso_propiedad_posiciones(portafolio_vacio, instrumento_test):
    # Esto cubre la línea 28 de portafolio.py
    pos = Posicion(instrumento_test, 10, 100)
    portafolio_vacio.agregar_posicion(pos)
    
    # Al acceder a .posiciones, cubrimos el getter
    assert len(portafolio_vacio.posiciones) == 1
    assert portafolio_vacio.posiciones[0].instrumento.ticker == instrumento_test.ticker