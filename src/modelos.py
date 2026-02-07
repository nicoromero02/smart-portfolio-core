from dataclasses import dataclass

@dataclass(frozen=True)
class Instrumento:
    """Instrumento financiero inmutable."""
    ticker: str
    tipo: str  # ej: "Acción", "Bono"
    sector: str

class Posicion:
    def __init__(self, instrumento: Instrumento, cantidad: float, precio_entrada: float):
        self.instrumento = instrumento
        self.precio_entrada = precio_entrada
        self.cantidad = cantidad  # Valida mediante el setter

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

    def calcular_ganancia_no_realizada(self, precio_actual: float) -> float:
        """
        Calcula el Profit and Loss (PnL) no realizado.
        Fórmula: $$PnL = (PrecioActual - PrecioEntrada) \times Cantidad$$
        """
        return (precio_actual - self.precio_entrada) * self.cantidad