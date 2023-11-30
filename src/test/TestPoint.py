import unittest
from ..labyrinth.two_dimension import Point

class TestPoint(unittest.TestCase):
    """
    Test of the class Point
    """

    def setUp(self):
        """
        Set up some basic points for the tests
        """
        # Create some points for testing
        self.point1 = Point(2, 3)
        self.point2 = Point(4, 5)
        self.point3 = Point(1, 2)

    def test_init(self):
        # Test initialization with default values
        point = Point()
        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 0)

    def test_repr(self):
        # Test the __repr__ method
        self.assertEqual(repr(self.point1), "(2,3)")
        self.assertEqual(repr(self.point2), "(4,5)")

    def test_eq(self):
        # Test the __eq__ method
        self.assertEqual(self.point1, Point(2, 3))
        self.assertNotEqual(self.point1, self.point2)

    def test_lt(self):
        # Test the __lt__ method
        self.assertTrue(self.point3 < self.point1)
        self.assertTrue(self.point1 < self.point2)
        self.assertFalse(self.point2 < self.point1)

    def test_le(self):
        # Test the __le__ method
        self.assertTrue(self.point3 <= self.point1)
        self.assertTrue(self.point1 <= self.point2)
        self.assertFalse(self.point2 <= self.point1)

    def test_gt(self):
        # Test the __gt__ method
        self.assertTrue(self.point2 > self.point1)
        self.assertTrue(self.point1 > self.point3)
        self.assertFalse(self.point1 > self.point2)

    def test_ge(self):
        # Test the __ge__ method
        self.assertTrue(self.point2 >= self.point1)
        self.assertTrue(self.point1 >= self.point3)
        self.assertFalse(self.point1 >= self.point2)

    def test_distance(self):
        # Test the distance method
        point1 = Point(1, 2)
        point2 = Point(4, 5)

        # Distance = sqrt((4-1)^2 + (5-2)^2) = sqrt(9 + 9) = sqrt(18)
        expected_distance = (18)**0.5

        self.assertEqual(point1.distance(point2), expected_distance)

    def test_manhattan_distance(self):
        # Test the manhattan_distance method
        point1 = Point(1, 2)
        point2 = Point(4, 5)

        # Manhattan Distance = |4-1| + |5-2| = 3 + 3 = 6
        expected_manhattan_distance = 6

        self.assertEqual(point1.manhattan_distance(point2), expected_manhattan_distance)


    def test_hash(self):
        # Test the __hash__ method
        self.assertEqual(hash(self.point1), hash(Point(2, 3)))
        self.assertNotEqual(hash(self.point1), hash(self.point2))

if __name__ == '__main__':
    unittest.main()
