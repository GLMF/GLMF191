import unittest
from Roman import Roman

class Romantest(unittest.TestCase):
    def setUp(self):
        self.roman = Roman(1)

    def test_partition_12(self):
        self.number = Roman(12)
        self.assertEqual(self.number._Roman__partition(), [12])

    def test_partition_123(self):
        self.number = Roman(123)
        self.assertEqual(self.number._Roman__partition(), [123])

    def test_partition_1234(self):
        self.number = Roman(1234)
        self.assertEqual(self.number._Roman__partition(), [234, 1])

    def test_partition_123456(self):
        self.number = Roman(123456)
        self.assertEqual(self.number._Roman__partition(), [456, 123])

    def test_partition_1234567(self):
        self.number = Roman(1234567)
        self.assertEqual(self.number._Roman__partition(), [567, 234, 1])


    def test_translateGroup_122(self):
        self.assertEqual(self.roman._Roman__translateGroup(122, 0), ('CXXII', 0))

    def test_translateGroup_4(self):
        self.assertEqual(self.roman._Roman__translateGroup(4, 1), ('MMMM', 0))

    def test_translateGroup_5(self):
        self.assertEqual(self.roman._Roman__translateGroup(5, 1), ('V', 1))

    def test_translateGroup_34(self):
        self.assertEqual(self.roman._Roman__translateGroup(34, 2), ('XXXIV', 2))


    def test_convert_123(self):
        self.number = Roman(123)
        self.assertEqual(self.number._Roman__convert(), 'CXXIII')

    def test_convert_63925(self):
        self.number = Roman(63925)
        self.assertEqual(self.number._Roman__convert(), '(LXIII)(1)CMXXV')

    def test_convert_14000022(self):
        self.number = Roman(14000022)
        self.assertEqual(self.number._Roman__convert(), '(XIV)(2)XXII')


if __name__ == '__main__':
    unittest.main()
