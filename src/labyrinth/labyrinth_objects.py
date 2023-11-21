from two_dimension import FiniteLine
from two_dimension import Axis
from two_dimension import Point
from UnAlingObjectError import UnAlingObjectError

class Wall(FiniteLine):
    """
    Simple wall representation in two dimensional plane

    The wall is parallel to X or Y axes,
    The wall width is infinitesimally small 
    and the height is infinitesimally large.
    The length of the Wall is variable.
    So the wall cant be jumped or traspased.

    Atributes:
        axis_state : Axis.ENUM
            Defines to wat axis is parallel the Wall
    """
    def __init__(self, left_or_botton: Point, right_or_top: Point):
        """
        Initialices the line of the wall and check if its parallel to an axis
        """
        super().__init__(left_or_botton, right_or_top)

        if self.isParalleltoX(): self.axis_state = Axis.X
        elif self.isParalleltoY(): self.axis_state = Axis.Y
        else: raise UnAlingObjectError("Error: Line is not parallel to X or Y axes")

class Door(Wall):
    """
    Simple Door implementation.

    The door is a passable wall but the 
    length of the door is always 1.

    Atributes
        DOOR_LENGTH : int
            DOOR_LENGTH = 1, length of the door
    """
    
    DOOR_LENGTH = 1

    def __init__(self, left_or_botton: Point, right_or_top: Point):

        super().__init__(left_or_botton, right_or_top)
        if self.length != self.DOOR_LENGTH:
            raise ValueError("Error: distance between points should be 1")
