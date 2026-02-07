from typing import List
from .modelos import Posicion

class PosicionNoExisteError(Exception):
    """Excepción para cuando buscamos un ticker que no está en el portafolio."""
    pass

class Portafolio:
    def __init__(self):
        # Tipado estricto para la lista de posiciones
        self._posiciones: List[Posicion] = []

    def agregar_posicion(self, posicion: Posicion) -> None:
        if not isinstance(posicion, Posicion):
            raise TypeError("Solo se pueden agregar objetos de tipo Posicion")
        self._posiciones.append(posicion)

    def remover_posicion(self, ticker: str) -> None:
        """Elimina una posición. Si no existe, lanza PosicionNoExisteError."""
        original_count = len(self._posiciones)
        self._posiciones = [p for p in self._posiciones if p.instrumento.ticker != ticker]
        
        if len(self._posiciones) == original_count:
            raise PosicionNoExisteError(f"No se encontró el activo con ticker: {ticker}")

    @property
    def posiciones(self) -> List[Posicion]:
        return self._posiciones