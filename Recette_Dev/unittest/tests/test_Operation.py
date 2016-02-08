import unittest
from src.Operation import Operation

class Operationtest(unittest.TestCase):
    def setUp(self):
        print('Lancement setUp()')
        self.fixture = Operation(2, 3)

    def tearDown(self):
        print('Lancement tearDown()')

    def test_simple_add(self):
        self.obj = Operation(2, 3)
        self.assertEqual(self.obj.add(), 2 + 3)

    def test_negatif_add(self):
        self.obj = Operation(-2, -3)
        self.assertEqual(self.obj.add(), 2 + -3)

if __name__ == '__main__':
    unittest.main()
