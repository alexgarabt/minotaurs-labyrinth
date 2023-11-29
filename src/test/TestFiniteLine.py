import unittest
from ..labyrinth.two_dimension import FiniteLine, Point 

class TestFiniteLine(unittest.TestCase):
    """
    Test of the class FiniteLine
    """

    def test_init(self):
        # Test initialization with different edge points
        point1 = Point(1, 2)
        point2 = Point(4, 5)
        point3 = Point(2, 3)

        line1 = FiniteLine(point1, point2)
        line2 = FiniteLine(point2, point3)

        self.assertEqual(line1.edge1, point1)
        self.assertEqual(line1.edge2, point2)
        self.assertEqual(line1.length, point1.distance(point2))

        self.assertEqual(line2.edge1, point2)
        self.assertEqual(line2.edge2, point3)
        self.assertEqual(line2.length, point2.distance(point3))

    def test_is_parallel_to_X(self):
        """
        Test lines parallel to x axis
        """
        # Test is_parallel_to_X method
        line1 = FiniteLine(Point(9, 5), Point(1, 5))  # parallel to X

        line2 = FiniteLine(Point(2, 10), Point(4, 3))  # not parallel to X

        self.assertTrue(line1.is_parallel_to_X())
        self.assertFalse(line2.is_parallel_to_X())

    def test_is_parallel_to_Y(self):
        """
        Test lines parallel to y axis
        """
        # Test is_parallel_to_Y method
        line1 = FiniteLine(Point(1, 3), Point(4, 2))  # not parallel to Y

        line2 = FiniteLine(Point(2, 3), Point(2, 5))  # parallel to Y

        self.assertTrue(line2.is_parallel_to_Y())
        self.assertFalse(line1.is_parallel_to_Y())

    def test_get_slope(self):
        """Test get_slope method"""
        
        line1 = FiniteLine(Point(1, 2), Point(4, 5))  # slope = (5-2)/(4-1) = 1
        line2 = FiniteLine(Point(2, 3), Point(2, 5))  # parallel to Y, slope = inf
        line3 = FiniteLine(Point(2,2), Point(6,2))    # parallel to X, slope = 0

        self.assertEqual(line1.get_slope(), 1)

        self.assertTrue(line3.is_parallel_to_X())
        self.assertEqual(line3.get_slope(), 0)

        self.assertTrue(line2.is_parallel_to_Y())
        self.assertEqual(line2.get_slope(), float('inf'))

    def test_is_parallel(self):
        """ Test is_parallel method """

        line1 = FiniteLine(Point(1, 2), Point(4, 5))  # slope = 1
        line3 = FiniteLine(Point(1, 1), Point(7, 7))  # slope = 1
        line4 = FiniteLine(Point(1, 8), Point(4, 5))  # slope = -1

        line2 = FiniteLine(Point(2, 3), Point(2, 5))  # parallel to Y, slope = inf
        
        self.assertTrue(line1.is_parallel(line3))
        self.assertTrue(line3.is_parallel(line1))

        self.assertTrue(line4.is_parallel(line1))
        self.assertTrue(line1.is_parallel(line4))

        self.assertFalse(line2.is_parallel(line1))

    def test_is_colinear(self):
        """ Test is_colinear method """
        line = FiniteLine(Point(1, 2), Point(4, 5))  # line passing through (1,2) and (4,5)

        self.assertTrue(line.is_colinear(Point(2, 3)))   # colinear point
        self.assertTrue(line.is_colinear(Point(0, 1)))   # colinear point
        self.assertTrue(line.is_colinear(Point(1, 2)))   # colinear point
        self.assertTrue(line.is_colinear(Point(4, 5)))   # colinear point
        self.assertTrue(line.is_colinear(Point(5, 6)))   # colinear point
        self.assertFalse(line.is_colinear(Point(6, 8)))  # not colinear point

    def test_contains(self):
        """ Test contains method """
        line = FiniteLine(Point(1, 2), Point(4, 5))  # line passing through (1,2) and (4,5)

        self.assertTrue(line.contains(Point(2, 3)))  # contained point
        self.assertTrue(line.contains(Point(1, 2)))  # contained point
        self.assertTrue(line.contains(Point(4, 5)))  # contained point
        self.assertFalse(line.contains(Point(6, 8)))  # not contained point

if __name__ == '__main__':
    unittest.main()
