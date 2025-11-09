# logic/estado_simulacion.py
from datetime import datetime, timedelta

class EstadoSimulacion:
    def __init__(self):
        self.hora_actual = datetime(2015, 3, 1, 7, 0)

    def avanzar_tiempo(self, minutos):
        """Simula que el tiempo avanza en la simulación."""
        self.hora_actual += timedelta(minutes=minutos)
