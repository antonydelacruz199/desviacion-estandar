class Desviacion:
    def __init__(self, datos):
        self.__datos = datos

    def desviacion_estandar(self):
        if len(self.__datos) == 0:
            return None
