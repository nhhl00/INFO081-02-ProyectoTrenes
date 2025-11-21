from models.estacion import Estacion

class GestorEstaciones:
    def __init__(self):
        self.estaciones = []

    def agregar(self, nombre, poblacion, vias):
        est = Estacion(nombre, poblacion, vias)
        self.estaciones.append(est)

    def buscar(self, nombre):
        for e in self.estaciones:
            if e.nombre == nombre:
                return e
        return None

    def eliminar(self, nombre):
        self.estaciones = [e for e in self.estaciones if e.nombre != nombre]
