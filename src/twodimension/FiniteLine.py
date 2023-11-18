from Point import Point
from Axis import Axis

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
      
    def contains(self, *args: [Point]) -> bool:
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