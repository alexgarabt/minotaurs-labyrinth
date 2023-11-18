from math import sqrt

import Point

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

    def __eq__(self, other: Point) -> bool:
        """
        Compares if the provided point is equal to this point
            
        Args: 
            other : Point
        return: 
            If the provided point is equal
        """
        return (self.x == other.x) and (self.y == other.y)

    def __lt__(self, other: Point) -> bool:
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
    
    def __le__(self, other: Point) -> bool:
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
    
    def __gt__(self, other: Point) -> bool:
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
    
    def __ge__(self, other: Point) -> bool:
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


    def distance(self, other: Point) -> float:
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