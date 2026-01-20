import unittest
from src.logica.Desviacion import Desviacion


class TestDesviacion(unittest.TestCase):
    def test_lista_vacia_retorna_none(self):
        datos = Desviacion([])
        self.assertIsNone(datos.desviacion_estandar())

    def test_un_elemento_retorna_cero(self):
        datos = Desviacion([5])
        self.assertEqual(0, datos.desviacion_estandar())
