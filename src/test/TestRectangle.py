import unittest
from ..labyrinth.two_dimension import Point, FiniteLine, Rectangle

class TestRectangle(unittest.TestCase):
    """ Test for Rectangle class"""
    
    def test_init(self):
        # Test initialization of the rectangle
        bottom_left = Point(1, 1)
        upper_left = Point(1, 4)
        bottom_right = Point(4, 1)
        upper_right = Point(4, 4)

        rectangle = Rectangle(bottom_left, upper_left, bottom_right, upper_right)

        self.assertEqual(rectangle.bottom_left, bottom_left)
        self.assertEqual(rectangle.upper_left, upper_left)
        self.assertEqual(rectangle.bottom_right, bottom_right)
        self.assertEqual(rectangle.upper_right, upper_right)

        self.assertIsInstance(rectangle.bottom_line, FiniteLine)
        self.assertIsInstance(rectangle.upper_line, FiniteLine)
        self.assertIsInstance(rectangle.righ_line, FiniteLine)
        self.assertIsInstance(rectangle.left_line, FiniteLine)

        self.assertEqual(rectangle.height, upper_left.distance(upper_right))
        self.assertEqual(rectangle.width, bottom_left.distance(bottom_right))

        expected_center = Point(2.5, 2.5)
        self.assertEqual(rectangle.center, expected_center)

    def test_contains(self):
        # Test the contains method
        bottom_left = Point(1, 1)
        upper_left = Point(1, 4)
        bottom_right = Point(4, 1)
        upper_right = Point(4, 4)

        rectangle = Rectangle(bottom_left, upper_left, bottom_right, upper_right)

        # Test points inside and outside the rectangle
        inside_point = Point(2, 3)
        outside_point = Point(5, 5)

        self.assertTrue(rectangle.contains(inside_point))
        self.assertFalse(rectangle.contains(outside_point))

    def test_distance(self):
        # Test the distance method
        bottom_left = Point(1, 1)
        upper_left = Point(1, 4)
        bottom_right = Point(4, 1)
        upper_right = Point(4, 4)

        rectangle = Rectangle(bottom_left, upper_left, bottom_right, upper_right)

        # Test distance from a point
        test_point = Point(3, 2)
        expected_distance = rectangle.center.distance(test_point)

        self.assertEqual(rectangle.distance(test_point), expected_distance)

    def test_hash(self):
        # Test the __hash__ method
        bottom_left1 = Point(1, 1)
        upper_left1 = Point(1, 4)
        bottom_right1 = Point(4, 1)
        upper_right1 = Point(4, 4)

        rectangle1 = Rectangle(bottom_left1, upper_left1, bottom_right1, upper_right1)

        bottom_left2 = Point(2, 2)
        upper_left2 = Point(2, 5)
        bottom_right2 = Point(5, 2)
        upper_right2 = Point(5, 5)

        rectangle2 = Rectangle(bottom_left2, upper_left2, bottom_right2, upper_right2)

        self.assertEqual(hash(rectangle1), hash((upper_left1, bottom_right1)))
        self.assertEqual(hash(rectangle2), hash((upper_left2, bottom_right2)))

if __name__ == '__main__':
    unittest.main()
