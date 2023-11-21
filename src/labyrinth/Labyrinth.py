from labyrinth_objects import Door
from labyrinth_objects import Wall
from two_dimension import Point

class Labyrinth:
    """
    Minotaurs Labyrinth representation, the labyrinth is made of Walls and Doors, 
    the walls aren't passables and the doors are.

    The labyrinth contains the minotaurs that is defined by his position and 
    we have Teseo that is also defined by his position.

    Minotaurs is inside the labyrinth and Teseo is outside.

    Teseo Position is in the origin of the coordenates in the plane (x=0, y=0)

    Atributtes:
        minotaurs : Point
            Minotaurs position inside of the Labyrinth
        teseo : Point
            Teseo postion outside of the Labyrinth
        _walls : 'list[Wall]'
            List with the walls of the Labyrinth
        _doors : 'list[Door]'
            List with the doors of the Labyrinth
    """

    def __init__(self, minotaurs: Point, walls: 'list[Wall]' = [], doors: 'list[Door]' = []):
        """
        Initializes the Labyrinth with the provided data

        Args:
            minotaurs : Point
                The position of the minotaurs
            walls : 'list[Wall]'
                List with the walls of the labyrinth
            doors: 'list[Door]'
                List with the doors of the labyrinth
        """
        self.minotaurs = minotaurs
        self._walls = walls
        self._doors = doors
        self.teseo = Point(0,0)     # Teseo is in the origin Postion


    def add_wall(self, wall: Wall):
        """
        Adds a wall into the wall list of the labyrinth
        """
        self.walls.append(wall)

    def add_door(self, door: Door):
        """
        Adds a wall into the wall list of the labyrinth
        """
        self.walls.append(door)