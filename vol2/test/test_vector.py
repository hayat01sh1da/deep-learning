import unittest
import numpy as np
import sys
sys.path.append('./src')
from vector import Vector

class TestVector(unittest.TestCase):
    def setUp(self):
        self.vector = Vector(np.array([1, 2, 3]))

    def test_get_class_name(self):
        self.assertEqual('<class 'numpy.ndarray'>', str(self.vector.x.__class__))

    def test_get_shape(self):
        self.assertEqual((3,), self.vector.x.shape)

    def test_get_dim(self):
        self.assertEqual(1, self.vector.x.ndim)

    def test_calc_inner_product(self):
        inner_product = self.vector.calc_inner_product(np.array([4, 5, 6]))
        self.assertEqual(32, inner_product)

if __name__ == '__main__':
    unittest.main()
