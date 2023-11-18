from labyrinth.Wall import Wall
from twodimension.Point import Point

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
