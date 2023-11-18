from twodimension.FiniteLine import FiniteLine
from twodimension.Point import Point
from twodimension.Axis import Axis
import labyrinth.UnAlingObjectError as UnAlingObjectError

class Wall(FiniteLine):
    """
    Simple wall representation in two dimensional plane

    The wall is parallel to X or Y axes,
    The wall width is infinitesimally small 
    and the height is infinitesimally large.
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

