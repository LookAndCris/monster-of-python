import unittest

def doblarNumeroLista(lista):
    """
    Función que devuelve el doble de los valores de la lista que se pasa como parámetro
    """
    return [n*2 for n in lista]

class PruebaDeCajaCristal(unittest.TestCase):

    # Los métodos setUp () y tearDown () permiten definir instrucciones que han de ser ejecutadas antes y después, 
    # respectivamente, de cada método de prueba. 
    # Se describen con mas detalle en la sección Organización del código de pruebas.

    def setUp(self) -> None:
        print("Método setUp antes de la prueba")
        return super().setUp()

    def test_doblar(self):
        """
        Casos de éxito
        """
        lista = [2, 4, 6, 8]
        resultado = doblarNumeroLista(lista)
        self.assertEqual(resultado, [4, 8, 12, 16])

    def test_doblar_vacia(self):
        """
        Casos de éxito
        """
        lista = []
        resultado = doblarNumeroLista(lista)
        self.assertEqual(resultado, [])

    def test_doblar_negativos(self):
        """
        Casos de éxito
        """
        lista = [-2, -4, -6, -8]
        resultado = doblarNumeroLista(lista)
        self.assertEqual(resultado, [-4, -8, -12, -16])

    def tearDown(self) -> None:
        print("Método tearDown después de la prueba")
        return super().tearDown()
    
if __name__ == '__main__':
    unittest.main()

# Ejecutar: python3 extra_unittest.py