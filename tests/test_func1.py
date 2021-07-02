import unittest
from moduloTestes.app.calc1 import calcula

call = calcula()


class TestCalc(unittest.TestCase):

    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(call.cal(5, 5), 10)

    def test_soma_2_2_4(self):
        self.assertEqual(call.cal(2, 2), 4)

    def test_func_com_sub_test(self):
        entradas = (
            (5, 5, 10),
            (12, 12, 24),
            (4, 4, 8)
        )
        for entrada in entradas:
            with self.subTest(entrada=entrada):
                a, b, saida = entrada
                self.assertEqual(call.cal(a, b),
                                 saida,
                                 msg=f'{a} + {b} não retornou {saida}'
                                 )


if __name__ == '__main__':
    unittest.main(verbosity=2)
