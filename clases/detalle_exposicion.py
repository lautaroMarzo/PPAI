from clases.obra import Obra


class Detalle_exposicion():
    def __init__(self, lugar_asignado, obra):
        self.lugar_asignado = lugar_asignado
        self.obra = obra

    # Metodo Get
    def get_lugar_asignado(self):
        return self.lugar_asignado

    def get_obra(self):
        return self.obra

    # Metodo Set
    def set_lugar_asignado(self, lugar_asignado):
        self.lugar_asignado = lugar_asignado

    def set_obra(self, obra):
        self.obra = obra

    # Este metodo llama al metodo get_duracion_extendida para obtener la duracion extendida de una obra.
    def buscar_durac_ext_obra(self):
        return Obra.get_duracion_extendida(self.obra)

