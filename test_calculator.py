import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    # add
    def test_add_true_1(self):
        self.assertEqual(self.calc.add(5, 7), 12)
    def test_add_true_2(self):
        self.assertEqual(self.calc.add(3, 5), 8)

    # sub
    def test_sub_true_1(self):
        self.assertEqual(self.calc.subtract(8, 2), 6)
    def test_sub_true_2(self):
        self.assertEqual(self.calc.subtract(9, 7), 2)

    # multi
    def test_multi_true_1(self):
        self.assertEqual(self.calc.multiply(8, 2), 16)
    def test_multi_true_2(self):
        self.assertEqual(self.calc.multiply(2, 7), 14)

    # divis
    def test_divis_true_1(self):
        self.assertEqual(self.calc.divide(20, 2), 10)
    def test_divis_true_2(self):
        self.assertEqual(self.calc.divide(21, 7), 3)
    
    # modu
    def test_modu_true_1(self):
        self.assertEqual(self.calc.modulo(19, 3), 1)
    def test_modu_true_2(self):
        self.assertEqual(self.calc.modulo(9, 5), 4)

if __name__ == '__main__':
    unittest.main()