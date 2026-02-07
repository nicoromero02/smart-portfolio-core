import pytest
from src.modelos import Instrumento
from src.portafolio import Portafolio

@pytest.fixture
def instrumento_test():
    """Fixture de un instrumento genérico."""
    return Instrumento(ticker="AAPL", tipo="Acción", sector="Tecnología")

@pytest.fixture
def portafolio_vacio():
    """Fixture de un portafolio inicializado sin datos."""
    return Portafolio()