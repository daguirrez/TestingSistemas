import unittest
import TiposNumero

class TestNumero(unittest.TestCase):
    def test_tipo(self):
        test_casos = [((51, -12, -3, 0, 2),"2 número(s) positivo(s)\n2 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)"),
                      ((0, 1, 2, 3, 4),"4 número(s) positivo(s)\n0 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)"),
                      ((-1, -2, -3), "0 número(s) positivo(s)\n3 número(s) negativo(s)\n1 número(s) par(es)\n2 número(s) impar(es)"),
                      ((0,),"0 número(s) positivo(s)\n0 número(s) negativo(s)\n1 número(s) par(es)\n0 número(s) impar(es)")]

        for numeros,esperado in test_casos:
            actual = TiposNumero.tipos_numeros(numeros)
            self.assertEqual(esperado,actual)

if __name__ == '__main__':
    unittest.main()