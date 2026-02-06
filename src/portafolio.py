from typing import List
from .modelos import Posicion

class Portafolio:
    def __init__(self):
        # Reto de Tipado: Lista que solo acepta objetos del tipo Posicion
        self._posiciones: List[Posicion] = []

    def agregar_posicion(self, posicion: Posicion) -> None:
        """Recibe un objeto Posicion y lo guarda en la lista"""
        if not isinstance(posicion, Posicion):
            raise TypeError("Solo se pueden agregar objetos de tipo Posicion")
        self._posiciones.append(posicion)

    @property
    def posiciones(self) -> List[Posicion]:
        """Expone las posiciones de forma controlada"""
        return self._posiciones