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


    def distance(self, other: 'Point') -> float:
        """
        Calculates the distance between this point and the provided one.
        
        It calculates the distance as sqrt((self.x  -other.x)^2 - (self.y - other.y)^2).
        """
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
    
    def getPointPair(self) -> (float,float):
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
       

    def isParalleltoX(self) -> bool:
        """
        Tells if the line is parallel to X axis.

        return:
            If the door is parallel to X axis return True
            Else return False
        """
        return (self.edge1.y - self.edge2.y) == 0
    
    def isParalleltoY(self) -> bool:
        """
        Tells if the line is parallel to Y axis.

        return:
            If the line is parallel to Y axis return True
            Else return False
        """
        return (self.edge1.x - self.edge2.x) == 0
    
    def isCo_Linear(self, point: Point) -> bool:
        """
        Tell if this line and the provided point are co-linear/
        could be contained in the same straigth line

        (x2-x1)(y3-y1) - (y2-y1)(x3-x1)=0
        """
        eq = ((self.edge2.x-self.edge1.x) * (point.y - self.edge1.y)) 
        - ((self.edge2.y-self.edge1.y) * (point.x - self.edge1.x))
        return eq == 0
      
    def contains(self, *args: 'list[Point]') -> bool:
        """
        Tells if the points in *args are contained in this line.

        A point is contained in a finite line 
        if is colinear with the line 
        and its distance with each edge points 
        are less than the length of distance
        between edge points
        """
        point_list = filter(lambda x:isinstance(x,Point),args)

        for point in list:
            if not(self.isCo_Linear(point)): 
                return False
            elif (point.distance(self.edge1) > self.length) or (point.distance(self.edge2) > self.length):
                return False
        
        return True