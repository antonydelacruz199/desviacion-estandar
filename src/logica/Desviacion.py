import math


class Desviacion:
    def __init__(self, datos):
        self.__datos = datos

    def desviacion_estandar(self):
        if len(self.__datos) == 0:
            return None

        promedio = sum(self.__datos) / len(self.__datos)
        suma = 0

        for x in self.__datos:
            suma += (x - promedio) ** 2

        return math.sqrt(suma / len(self.__datos))