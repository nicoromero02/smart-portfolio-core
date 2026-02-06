from dataclasses import dataclass

@dataclass(frozen=True)
class Instrumento:
    """Clase inmutable para activos financieros"""
    ticker: str
    tipo: str
    sector: str

class Posicion:
    def __init__(self, instrumento: Instrumento, cantidad: float, precio_entrada: float):
        self.instrumento = instrumento
        self.precio_entrada = precio_entrada
        self.cantidad = cantidad

    @property
    def cantidad(self) -> float:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor: float):
        if valor < 0:
            raise ValueError("La cantidad NO puede ser negativa.")
        self._cantidad = valor

    def calcular_valor_actual(self, precio_mercado: float) -> float:
        return self.cantidad * precio_mercado