from typing import List
from .modelos import Posicion

class PosicionNoExisteError(Exception):
    """Excepción lanzada cuando se intenta operar un activo que no está en el portafolio."""
    pass

class Portafolio:
    def __init__(self):
        self._posiciones: List[Posicion] = []

    def agregar_posicion(self, posicion: Posicion) -> None:
        self._posiciones.append(posicion)

    def remover_posicion(self, ticker: str) -> None:
        """
        Elimina una posición por su ticker. 
        Lanza PosicionNoExisteError si no se encuentra.
        """
        encontrado = False
        for i, pos in enumerate(self._posiciones):
            if pos.instrumento.ticker == ticker:
                self._posiciones.pop(i)
                encontrado = True
                break
        
        if not encontrado:
            raise PosicionNoExisteError(f"No existe el activo con ticker: {ticker}")

    @property
    def posiciones(self) -> List[Posicion]:
        return self._posiciones