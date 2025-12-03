"""
Módulo de Modelos - Clase
Modela una clase del gimnasio (ej. Spinning, Yoga) con cupo e inscritos.
"""
from typing import List, Any, Optional
from datetime import date, time


class Clase:
    """Representa una clase programada.

    Atributos:
        id (int): identificador
        nombre (str)
        instructor: referencia a Instructor
        cupo_maximo (int)
        fecha (date)
        hora (time)
        inscritos (List): lista de socios inscritos
    """

    def __init__(self, clase_id: int, nombre: str, instructor: Any, cupo_maximo: int, fecha: date, hora: time):
        if cupo_maximo <= 0:
            raise ValueError("El cupo máximo debe ser mayor que 0")

        self.id: int = int(clase_id)
        self.nombre: str = nombre
        self.instructor = instructor
        self.cupo_maximo: int = int(cupo_maximo)
        self.fecha: date = fecha
        self.hora: time = hora
        self.inscritos: List[Any] = []