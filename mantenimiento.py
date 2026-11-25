
class Mantenimiento:
    def __init__(self, fecha, descripcion, tecnico):
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tecnico = tecnico

    @property
    def fecha(self):
        return self.__fecha

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def tecnico(self):
        return self.__tecnico

    def mostrar_informacion(self):
        return (
            f"Fecha: {self.fecha}\n"
            f"Descripción: {self.descripcion}\n"
            f"Técnico: {self.tecnico}"
        )
