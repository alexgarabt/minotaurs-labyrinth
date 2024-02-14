import unittest
from labyrinth.two_dimension import FiniteLine, Point, Rectangle
from labyrinth.Labyrinth import Labyrinth
from labyrinth.labyrinth_objects import Wall, Door

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

    def test_contains_point(self):
        """ Test contains point method """
        line = FiniteLine(Point(1, 2), Point(4, 5))  # line passing through (1,2) and (4,5)

        self.assertTrue(line.contains_point(Point(2, 3)))  # contained point
        self.assertTrue(line.contains_point(Point(1, 2)))  # contained point
        self.assertTrue(line.contains_point(Point(4, 5)))  # contained point
        self.assertFalse(line.contains_point(Point(6, 8)))  # not contained point

    def test_contains_line(self):
        """ Test contains line method """
        line = FiniteLine(Point(1, 2), Point(4, 5))  # line passing through (1,2) and (4,5)
        line2 = FiniteLine(Point(1, 2), Point(2, 3))
        line3 = FiniteLine(Point(6,8), Point(9,3))

        self.assertTrue(line.contains_line(line)) #contains it self
        self.assertTrue(line.contains_line(line2))

        self.assertFalse(line2.contains_line(line))

        self.assertFalse(line3.contains_line(line))
        self.assertFalse(line.contains_line(line3))



class TestRectangle(unittest.TestCase):

    def setUp(self):
        # Create a sample rectangle for testing
        self.bottom_left = Point(1, 1)
        self.upper_left = Point(1, 4)
        self.bottom_right = Point(4, 1)
        self.upper_right = Point(4, 4)
        self.center = Point(2.5, 2.5)
        self.height = 3
        self.width = 3
        self.rectangle = Rectangle(
            bottom_left=self.bottom_left,
            upper_left=self.upper_left,
            bottom_right=self.bottom_right,
            upper_right=self.upper_right
        )

    def test_contains(self):
        # Test the contains method
        inside_point = Point(2, 3)
        outside_point = Point(5, 5)

        self.assertTrue(self.rectangle.contains(inside_point))
        self.assertFalse(self.rectangle.contains(outside_point))

    def test_distance(self):
        # Test the distance method
        test_point = Point(3, 2)
        expected_distance = self.center.distance(test_point)

        self.assertEqual(self.rectangle.distance(test_point), expected_distance)

    def test_manhattan_distance(self):
        # Test the manhattan_distance method
        test_point = Point(3, 2)
        expected_manhattan_distance = abs(self.center.x - test_point.x) + abs(self.center.y - test_point.y)

        self.assertEqual(self.rectangle.manhattan_distance(test_point), expected_manhattan_distance)

    def test_hash(self):
        # Test the __hash__ method
        expected_hash = hash((self.upper_left, self.bottom_right))
        self.assertEqual(hash(self.rectangle), expected_hash)
    
class TestLabyrinth(unittest.TestCase):
    """Test for Labyrinth class and the A* search algorithm"""
        

    def test_search_labyrinth_1(self):
        """
        Test labyrinth search, with solution
        """
        #Initialize doors and walls

        labyrinth: Labyrinth= Labyrinth(max_area=6)

        doors = []
        walls = []
        doors.append(Door(Point(1,2),Point(2,2)))
        doors.append(Door(Point(2,1),Point(2,2)))
        doors.append(Door(Point(3,1),Point(3,2)))
        doors.append(Door(Point(2,2),Point(2,3)))
        doors.append(Door(Point(3,2),Point(3,3)))
        doors.append(Door(Point(3,3),Point(4,3)))
        doors.append(Door(Point(2,3),Point(2,4)))
        doors.append(Door(Point(3,3),Point(3,4)))
        doors.append(Door(Point(4,3),Point(4,4)))
        
        walls.append(Wall(Point(1,1), Point(1,4)))
        walls.append(Wall(Point(2,1), Point(2,4)))
        walls.append(Wall(Point(3,1), Point(3,4)))
        walls.append(Wall(Point(4,1), Point(4,4)))
        walls.append(Wall(Point(1,1), Point(4,1)))
        walls.append(Wall(Point(1,2), Point(4,2)))
        walls.append(Wall(Point(1,3), Point(4,3)))
        walls.append(Wall(Point(1,4), Point(4,4)))

        minotaurs: Point = Point(1.5, 1.5)

        labyrinth.minotaurs = minotaurs
        labyrinth.add_labyrinth_objs(walls, doors)

        list_result = labyrinth.teseo_to_minotaurs()
        is_possible = list_result[0]
        path = list_result[1]
        number_of_nodes_used = len(path)
        number_of_doors_used = list_result[2]

        labyrinth.print_path_teseo_to_minotaurs()
        labyrinth.print_solution(use_info=True)

        self.assertTrue(is_possible)               # Check that is possible to resolve the labyrinth
        self.assertEqual(number_of_doors_used, 5)  # The min path uses 5 doors
        self.assertEqual(number_of_nodes_used, 13) # The min path uses 13 nodes
    
    def test_search_labyrinth_2_no_solution(self):
        
        labyrinth: Labyrinth = Labyrinth(max_area=6)
        doors = []
        walls = []

        walls.append(Wall(Point(1,1), Point(2,1)))
        walls.append(Wall(Point(1,1), Point(1,2)))
        walls.append(Wall(Point(2,1), Point(2,2)))
        walls.append(Wall(Point(1,2), Point(2,2)))

        labyrinth.minotaurs = Point(1.5, 1.7)
        labyrinth.add_labyrinth_objs(walls, doors)

        list_result = labyrinth.teseo_to_minotaurs()
        is_possible = list_result[0]
        path = list_result[1]
        number_of_nodes_used = len(path)
        number_of_doors_used = list_result[2]

        #labyrinth.print_path_teseo_to_minotaurs()
        #labyrinth.print_solution()

        self.assertFalse(is_possible)              # Check that is not possible to resolve the labyrinth
        self.assertEqual(number_of_doors_used, 0) 
        self.assertEqual(number_of_nodes_used, 0)

    def test_search_labyrinth_3(self):
        
        labyrinth: Labyrinth = Labyrinth(max_area=10)
        #29 21
        doors = []
        walls = []

        walls.append(Wall(Point(1,1), Point(1,5)))
        walls.append(Wall(Point(1,6), Point(1,8)))
        walls.append(Wall(Point(2,1), Point(2,2)))
        walls.append(Wall(Point(2,3), Point(2,4)))
        walls.append(Wall(Point(3,1), Point(3,2)))
        walls.append(Wall(Point(3,3), Point(3,4)))
        walls.append(Wall(Point(3,5), Point(3,7)))
        walls.append(Wall(Point(4,1), Point(4,8)))
        walls.append(Wall(Point(5,1), Point(5,2)))
        walls.append(Wall(Point(5,3), Point(5,8)))
        walls.append(Wall(Point(6,4), Point(6,8)))
        walls.append(Wall(Point(7,1), Point(7,2)))
        walls.append(Wall(Point(7,3), Point(7,4)))
        walls.append(Wall(Point(7,5), Point(7,8)))
        walls.append(Wall(Point(8,1), Point(8,8)))
        walls.append(Wall(Point(1,1), Point(4,1)))
        walls.append(Wall(Point(5,1), Point(7,1)))
        walls.append(Wall(Point(1,2), Point(2,2)))
        walls.append(Wall(Point(3,2), Point(5,2)))
        walls.append(Wall(Point(2,3), Point(5,3)))
        walls.append(Wall(Point(7,3), Point(8,3)))
        walls.append(Wall(Point(3,4), Point(6,4)))
        walls.append(Wall(Point(7,4), Point(8,4)))
        walls.append(Wall(Point(1,5), Point(2,5)))
        walls.append(Wall(Point(3,5), Point(8,5)))
        walls.append(Wall(Point(2,6), Point(8,6)))
        walls.append(Wall(Point(3,7), Point(8,7)))
        walls.append(Wall(Point(1,8), Point(3,8)))
        walls.append(Wall(Point(4,8), Point(8,8)))

        doors.append(Door(Point(1,5), Point(1,6)))
        doors.append(Door(Point(2,2), Point(2,3)))
        doors.append(Door(Point(2,5), Point(2,6)))
        doors.append(Door(Point(3,2), Point(3,3)))
        doors.append(Door(Point(3,4), Point(3,5)))
        doors.append(Door(Point(3,7), Point(3,8)))
        doors.append(Door(Point(6,1), Point(6,2)))
        doors.append(Door(Point(7,2), Point(7,3)))
        doors.append(Door(Point(7,4), Point(7,5)))
        doors.append(Door(Point(4,1), Point(5,1)))
        doors.append(Door(Point(2,2), Point(3,2)))
        doors.append(Door(Point(5,2), Point(6,2)))
        doors.append(Door(Point(5,3), Point(6,3)))
        doors.append(Door(Point(6,3), Point(7,3)))
        doors.append(Door(Point(1,4), Point(2,4)))
        doors.append(Door(Point(2,4), Point(3,4)))
        doors.append(Door(Point(6,4), Point(7,4)))
        doors.append(Door(Point(1,6), Point(2,6)))
        doors.append(Door(Point(1,7), Point(2,7)))
        doors.append(Door(Point(2,7), Point(3,7)))
        doors.append(Door(Point(3,8), Point(4,8)))


        minotaurs = Point(2.6,7.1)

        labyrinth.minotaurs = minotaurs
        labyrinth.add_labyrinth_objs(walls=walls, doors=doors)

        list_result = labyrinth.teseo_to_minotaurs()
        is_possible = list_result[0]
        path = list_result[1]
        number_of_nodes_used = len(path)
        number_of_doors_used = list_result[2]

        #labyrinth.print_path_teseo_to_minotaurs()
        #labyrinth.print_solution()

        self.assertTrue(is_possible)              
        self.assertEqual(number_of_doors_used, 2)  # The min path uses doors
        self.assertEqual(number_of_nodes_used, 14) # The min path uses  nodes

    def test_search_labyrinth_4(self):
        """Test max distance path but less doors used"""
        labyrinth: Labyrinth = Labyrinth(max_area=11)
        #29 21
        doors = []
        walls = []

        walls.append(Wall(Point(1,1), Point(1,5)))
        walls.append(Wall(Point(1,6), Point(1,9)))
        walls.append(Wall(Point(2,5), Point(2,9)))
        walls.append(Wall(Point(3,3), Point(3,4)))
        walls.append(Wall(Point(3,5), Point(3,7)))
        walls.append(Wall(Point(3,8), Point(3,9)))
        walls.append(Wall(Point(4,1), Point(4,2)))
        walls.append(Wall(Point(4,3), Point(4,4)))
        walls.append(Wall(Point(4,7), Point(4,9)))
        walls.append(Wall(Point(5,3), Point(5,4)))
        walls.append(Wall(Point(6,3), Point(6,4)))
        walls.append(Wall(Point(7,1), Point(7,2)))
        walls.append(Wall(Point(7,3), Point(7,5)))
        walls.append(Wall(Point(7,6), Point(7,9)))
        walls.append(Wall(Point(8,1), Point(8,2)))
        walls.append(Wall(Point(8,3), Point(8,9)))
        walls.append(Wall(Point(9,1), Point(9,9)))
        walls.append(Wall(Point(1,1), Point(5,1)))
        walls.append(Wall(Point(7,1), Point(9,1)))
        walls.append(Wall(Point(1,2), Point(2,2)))
        walls.append(Wall(Point(5,2), Point(6,2)))
        walls.append(Wall(Point(7,2), Point(9,2)))
        walls.append(Wall(Point(5,3), Point(6,3)))
        walls.append(Wall(Point(7,3), Point(9,3)))
        walls.append(Wall(Point(5,4), Point(6,4)))
        walls.append(Wall(Point(7,4), Point(9,4)))
        walls.append(Wall(Point(2,5), Point(3,5)))
        walls.append(Wall(Point(7,5), Point(9,5)))
        walls.append(Wall(Point(1,6), Point(3,6)))
        walls.append(Wall(Point(6,6), Point(9,6)))
        walls.append(Wall(Point(1,7), Point(3,7)))
        walls.append(Wall(Point(6,7), Point(9,7)))
        walls.append(Wall(Point(1,8), Point(3,8)))
        walls.append(Wall(Point(4,8), Point(5,8)))
        walls.append(Wall(Point(7,8), Point(9,8)))
        walls.append(Wall(Point(1,9), Point(3,9)))
        walls.append(Wall(Point(4,9), Point(9,9)))

        doors.append(Door(Point(2,1), Point(2,2)))
        doors.append(Door(Point(2,2), Point(2,3)))
        doors.append(Door(Point(2,3), Point(2,4)))
        doors.append(Door(Point(2,4), Point(2,5)))
        doors.append(Door(Point(3,4), Point(3,5)))
        doors.append(Door(Point(4,2), Point(4,3)))
        doors.append(Door(Point(4,4), Point(4,5)))
        doors.append(Door(Point(4,5), Point(4,6)))
        doors.append(Door(Point(5,5), Point(5,6)))
        doors.append(Door(Point(5,8), Point(5,9)))
        doors.append(Door(Point(6,2), Point(6,3)))
        doors.append(Door(Point(6,8), Point(6,9)))
        doors.append(Door(Point(7,5), Point(7,6)))
        doors.append(Door(Point(3,2), Point(4,2)))
        doors.append(Door(Point(4,2), Point(5,2)))
        doors.append(Door(Point(6,2), Point(7,2)))
        doors.append(Door(Point(3,3), Point(4,3)))
        doors.append(Door(Point(3,4), Point(4,4)))
        doors.append(Door(Point(1,5), Point(2,5)))
        doors.append(Door(Point(5,5), Point(6,5)))
        doors.append(Door(Point(6,5), Point(7,5)))
        doors.append(Door(Point(5,6), Point(6,6)))
        doors.append(Door(Point(5,8), Point(6,8)))

        minotaurs = Point(7.7,2.1)

        labyrinth.minotaurs = minotaurs
        labyrinth.add_labyrinth_objs(walls=walls, doors=doors)

        list_result = labyrinth.teseo_to_minotaurs()
        is_possible = list_result[0]
        path = list_result[1]
        number_of_nodes_used = len(path)
        number_of_doors_used = list_result[2]

        #labyrinth.print_path_teseo_to_minotaurs()
        #labyrinth.print_solution()

        self.assertTrue(is_possible)              # Check that is  possible to resolve the labyrinth
        self.assertEqual(number_of_doors_used, 9)  # The min path uses doors
        self.assertEqual(number_of_nodes_used, 16) # The min path uses  nodes

    
if __name__ == '__main__':
    unittest.main()
    
    

