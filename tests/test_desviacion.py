import unittest
from src.logica.Desviacion import Desviacion


class TestDesviacion(unittest.TestCase):
    def test_lista_vacia_retorna_none(self):
        datos = Desviacion([])
        self.assertIsNone(datos.desviacion_estandar())
