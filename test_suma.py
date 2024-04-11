# test_suma.py

# Librería para pruebas unitarias
import unittest
from suma import sumar

# Clase que recibe una prueba unitaria
class TestSumar(unittest.TestCase):

    # Método con tres llamadas a funciones assertEqual
    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()