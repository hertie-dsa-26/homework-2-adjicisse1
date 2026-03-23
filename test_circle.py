import unittest
from circle import Circle
import math

class TestCircle(unittest.TestCase):

    def test_perimeter(self):
        c = Circle(1)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi)

        c = Circle(2)
        self.assertAlmostEqual(c.perimeter(), 4 * math.pi)

    def test_area(self):
        c = Circle(1)
        self.assertAlmostEqual(c.area(), math.pi)

        c = Circle(2)
        self.assertAlmostEqual(c.area(), 4 * math.pi)


if __name__ == '__main__':
    unittest.main()