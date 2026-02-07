import pytest
from src.reportes import ReportadorFinanciero
from src.portafolio import Portafolio
from src.modelos import Posicion, Instrumento

def test_reporte_impresion_completa(capsys, instrumento_test):
    # Preparamos los datos
    portafolio = Portafolio()
    posicion = Posicion(instrumento_test, 10, 100.0)
    portafolio.agregar_posicion(posicion)
    
    # Ejecutamos
    reportador = ReportadorFinanciero()
    reportador.imprimir_resumen(portafolio)
    
    # Verificamos salida
    captured = capsys.readouterr()
    assert "RESUMEN DE INVERSIONES" in captured.out
    assert instrumento_test.ticker in captured.out