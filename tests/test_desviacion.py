import unittest
from src.logica.Desviacion import Desviacion


class TestDesviacion(unittest.TestCase):
    def test_lista_vacia_retorna_none(self):
        datos = Desviacion([])
        self.assertIsNone(datos.desviacion_estandar())

    def test_un_elemento_retorna_cero(self):
        datos = Desviacion([5])
        self.assertEqual(0, datos.desviacion_estandar())

    def test_n_elementos(self):
        datos = Desviacion([2, 4, 4, 4, 5, 5, 7, 9])
        self.assertEqual(2, datos.desviacion_estandar())
