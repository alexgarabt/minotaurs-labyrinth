from enum import Enum
from math import sqrt

class Axis(Enum):
    """
    Represents dimensional axes
    """ 
    X = 1
    Y = 2
    Z = 3
    # ...


class Point:
    """
    Point in two dimensional representation.

    Point its be represented as the pair (x,y),
    contains an (X) and (Y) point.

    Atributtes:
        self.x : float
        self.y : float
    """

    def __init__(self, x: float=0, y: float=0):
        """
        Initialices the Point into the (x,y) pair.

        If there is now arguments provided it initialices 
        the point into the origin point of X and Y axis.
        """
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Returns a String representation of the point -> (x,y)"""
        return "".join(["(",str(self.x),",",str(self.y),")"])

    def __eq__(self, other: 'Point') -> bool:
        """
        Compares if the provided point is equal to this point
            
        Args: 
            other : Point
        return: 
            If the provided point is equal
        """
        if not(isinstance(other, Point)): return False
        return (self.x == other.x) and (self.y == other.y)

    def __lt__(self, other: 'Point') -> bool:
        """
        Compares points based on their distance from the origin

        Args: 
            other : Point
        return: 
            If this point is less than the provided point
        """
        self_distance = self.distance(Point(0,0))
        other_distance = other.distance(Point(0,0))
        return self_distance < other_distance
    
    def __le__(self, other: 'Point') -> bool:
        """
        Compares points based on their distance from the origin

        Args: 
            other : Point
        return: 
            If this point is less or equal than the provided point
        """
        self_distance = self.distance(Point(0,0))
        other_distance = other.distance(Point(0,0))
        return self_distance <= other_distance
    
    def __gt__(self, other: 'Point') -> bool:
        """
        Compares points based on their distance from the origin

        Args: 
            other : Point
        return: 
            If this point is great than the provided point
        """
        self_distance = self.distance(Point(0,0))
        other_distance = other.distance(Point(0,0))
        return self_distance > other_distance
    
    def __ge__(self, other: 'Point') -> bool:
        """
        Compares points based on their distance from the origin

        Args: 
            other : Point
        return: 
            If this point is great or equals than the provided point
        """
        self_distance = self.distance(Point(0,0))
        other_distance = other.distance(Point(0,0))
        return self_distance >= other_distance   

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def distance(self, other: 'Point') -> float:
        """
        Calculates the distance between this point and the provided one.
        
        It calculates the distance as sqrt((self.x  -other.x)^2 - (self.y - other.y)^2).
        """
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
    
    def manhattan_distance(self, other: 'Point') -> float:
        """
        Calculates the distance between this point and the provided one 
        using manhattan distance.

        Manhattan distance = |self.x - other.x| + |self.y - other.y|
        """
        return abs(self.x - other.x) + abs(self.y - other.y)
    

    def get_point_pair(self) -> (float,float):
        """
        Get the point into a (x,y) format

        return:
            A (float, float) tuple as (x,y)
        """
        return (self.x, self.y)
    
class FiniteLine:
    """
    Simple representation of a  finite line in a 2 dimemensional way,
    The border is infinitely small so it doesn't have width.
    
    Atributes:
        self.edge_1 : Point
            Left or botton edge of the line and its represented by the point in (x,y).
        selg.edge2 : Point
            Right or top edge of the line and its represented by the point in (x,y).
        self.leght : float
            Length of the line must be the distance between the edge points of the line
        
        !Edge points should be different points

    """

    def __init__(self, left_or_botton: Point, right_or_top: Point):
        """
        Initialize the line.

        Get the edge points of the line and represent the line

        raise:
            UnAlignObjectError
                When the line is not parallel to X or Y axes.
        """
        self.edge1 = left_or_botton
        self.edge2 = right_or_top
        self.length = self.edge1.distance(self.edge2)

    def is_parallel_to_X(self) -> bool:
        """
        Tells if the line is parallel to X axis.

        return:
            If the door is parallel to X axis return True
            Else return False
        """
        return (self.edge1.y - self.edge2.y) == 0
    
    def is_parallel_to_Y(self) -> bool:
        """
        Tells if the line is parallel to Y axis.

        return:
            If the line is parallel to Y axis return True
            Else return False
        """
        return (self.edge1.x - self.edge2.x) == 0
    
    def get_slope(self) -> float:
        """
        Returns the slope of this straight line

        returns:
            Inifinite = float('inf'), if this line is parallel to Y axis.
            Normal float slope in other case.
        """

        if self.is_parallel_to_Y(): return float('inf')
        elif self.is_parallel_to_X(): return 0

        return ((self.edge2.y - self.edge1.y) / (self.edge2.x - self.edge1.x))
    
    def is_parallel(self, other_line: 'FiniteLine') -> bool:
        """
        Tells if two lines are parallel

        Two lines are parallel if they have the same |slope| is absolute value
        """

        return abs(self.get_slope()) == abs(other_line.get_slope())

    def is_colinear(self, point: Point) -> bool:
        """
        Tell if this line and the provided point are co-linear/
        could be contained in the same straigth inifite line

        (x2-x1)(y3-y1) - (y2-y1)(x3-x1)=0

        TODO check if abs() is needed
        """
        eq = ((self.edge2.x - self.edge1.x) * (point.y - self.edge1.y)) - ((self.edge2.y-self.edge1.y) * (point.x - self.edge1.x))
        return eq == 0
      
    def contains_point(self, *args: 'list[Point]') -> bool:
        """
        Tells if the points in *args are contained in this line.

        A point is contained in a finite line 
        if is colinear with the line 
        and its distance with each edge points 
        are less than the length of distance
        between edge points
        """
        point_list = filter(lambda x:isinstance(x,Point),args)

        for point in point_list:
            if not(self.is_colinear(point)): 
                return False
            elif (point.distance(self.edge1) > self.length) or (point.distance(self.edge2) > self.length):
                return False
        
        return True
    
    def contains_line(self, contained_line: 'FiniteLine') -> bool:
        """
        Tells if the provided line is contaned in this one
        """ 
        return self.contains_point(contained_line.edge1, contained_line.edge2)
    
    def __repr__(self) -> str:
        """Returns a String representation of the point -> (x,y)"""
        return "".join(["Line(", self.edge1.__repr__(), ", ", self.edge2.__repr__(), ")"])
    
    def __hash__(self) -> int:
        return hash((self.edge1, self.edge2))
    
    def __eq__(self, other: 'FiniteLine') -> bool:
        if not(isinstance(other, FiniteLine)): return False
        return (self.edge1 == other.edge1) and (self.edge2 == other.edge2)

class Rectangle:
    """
    Rectangle in 2 dimension that is defined by 4 edge points and 4 edge finites lines

    Points should be aling into straight line show the edge lines will be parallel two for two

    Atributes:
        bottom_left: Point
            should be aling with upper_left & bottom_right
        upper_left: Point
            should be aling with upper_right & bottom_left  
        bottom_right: Point
        upper_right: Point

        bottom_line 
        upper_line 
        righ_line 
        left_line
    """
    def __init__(self, 
                 bottom_left: Point = None, 
                 upper_left: Point = None, 
                 bottom_right: Point = None, 
                 upper_right: Point = None, 
                 center: Point = None, 
                 height: float = None, 
                 width: float = None):
        if (bottom_left is not None and upper_left is not None and 
            bottom_right is not None and upper_right is not None):
            # First constructor logic
            self.bottom_left = bottom_left
            self.upper_left = upper_left
            self.upper_right = upper_right
            self.bottom_right = bottom_right

            # Define the four lines of the rectangle
            self.bottom_line = FiniteLine(self.bottom_left, self.bottom_right)
            self.upper_line = FiniteLine(self.upper_left, self.upper_right)
            self.right_line = FiniteLine(self.bottom_right, self.upper_right)
            self.left_line = FiniteLine(self.bottom_left, self.upper_left)

            # Define data of rectangle
            self.height = self.upper_line.length
            self.width = self.bottom_line.length

            # Create the center point of the rectangle
            center_x = self.bottom_left.x + (self.width / 2)
            center_y = self.bottom_left.y + (self.height / 2)
            self.center = Point(center_x, center_y)

        elif center is not None and height is not None and width is not None:
            # Second constructor logic
            self.center = center
            self.height = height
            self.width = width

            self.bottom_left = Point((self.center.x - width/2), (self.center.y - height/2))
            self.upper_left = Point(self.bottom_left.x, self.bottom_left.y + height)
            self.upper_right = Point(self.upper_left.x + width, self.upper_left.y)
            self.bottom_right = Point(self.bottom_left.x + width, self.bottom_left.y)

            # Define the four lines of the rectangle
            self.bottom_line = FiniteLine(self.bottom_left, self.bottom_right)
            self.upper_line = FiniteLine(self.upper_left, self.upper_right)
            self.right_line = FiniteLine(self.bottom_right, self.upper_right)
            self.left_line = FiniteLine(self.bottom_left, self.upper_left)

        else:
            raise ValueError("Invalid parameters for Rectangle constructor")

    def contains(self, point: Point) -> bool:
        """
        Tells if a point is inside of the rectangle 
        (includes also the edges)

        Args:
            point: Point
                Point to check if its inside of the rectangle
        return:
            True if the point is inside of the rectangle
            False if other case
        """
        inside_width = abs((point.x - self.center.x )) <= (self.width/2)
        inside_height = abs((point.y - self.center.y)) <= (self.height/2)
        
        return (inside_width and inside_height)
    
    def distance(self, point: Point) -> float:
        """
        Return the distance bettween this rectangle and the point

        The distance is calculate from the center point and the provided point
        """
        return self.center.distance(point)

    def manhattan_distance(self, other: Point) -> float:
        """
        Calculates the distance between the center of this rectangle and the provided one 
        using manhattan distance.

        Manhattan distance = |self.center.x - other.x| + |self.center.y - other.y|
        """
        return abs(self.center.x - other.x) + abs(self.center.y - other.y)
    
    def __hash__(self) -> int:
        """
        The hash is calculate as the hash of a tuple how contains two points
        """
        return hash((self.upper_left, self.bottom_right))
    
    def __eq__(self, other: 'Rectangle'):
        if not(isinstance(other, Rectangle)): return False
        conditions = (self.center == other.center) and (self.height == other.height) and (self.width == self.width)
    
    def __repr__(self) -> str:
        """Returns a String representation of the Rectangle-> center point, height and width"""
        return "".join(["Rectangle: Center", self.center.__repr__(), ", Height: ", self.height.__repr__(), ", Width: ", self.width.__repr__()])
    

    
    

