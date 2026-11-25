

from abc import ABC, abstractmethod


class Equipo(ABC):
    def __init__(self, marca, capacidad, modelo):
        self.__marca = marca
        self.__capacidad = capacidad
        self.__modelo = modelo
        self.__mantenimientos = []

    @property
    def marca(self):
        return self.__marca

    @property
    def capacidad(self):
        return self.__capacidad

    @property
    def modelo(self):
        return self.__modelo

    @property
    def mantenimientos(self):
        return self.__mantenimientos

    def agregar_mantenimiento(self, mantenimiento):
        self.__mantenimientos.append(mantenimiento)

    @abstractmethod
    def obtener_tipo(self):
        pass

    def mostrar_informacion(self):
        return f"{self.marca} - {self.capacidad} BTU - {self.modelo} - {self.obtener_tipo()}"


class AireConvencional(Equipo):
    def obtener_tipo(self):
        return "Convencional"


class AireInverter(Equipo):
    def obtener_tipo(self):
        return "Inverter"
