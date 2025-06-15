import unittest
from helpers.lagrange import lagrange

class TestLagrange(unittest.TestCase):
    def test_linear_interpolation(self):
        data = ((1, 2), (3, 4))
        self.assertEqual(
                3,
                lagrange(data, 2)
        )

if __name__ == '__main__':
    unittest.main()
