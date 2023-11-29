from labyrinth_objects import Door, Wall
from two_dimension import Point, Rectangle
from graphs import CellNode, GridCellGraph


#TODO implen the dictionary of nodes and create graph node and add doors
class Labyrinth:
    """
    Minotaurs Labyrinth representation, the labyrinth is made of Walls and Doors, 
    the walls aren't passables and the doors are.

    The labyrinth contains the minotaurs that is defined by his position and 
    we have Teseo that is also defined by his position.

    The dimensions of the labyrinth are inside [1,199] for X and Y plane

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
        _labyrinth_graph: GridCellGraph
            Graph structure of nodes how is difined by the labyrinth
        _nodes_dictionary: 'dictionary{hash:Node}'
    """
    LABYRINTH_COODRS = range(1,299)
    CELL_AREA = 1 # 1 (unit^2), area of sectors, the min area of a cell in the labyrinth map

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
        self.nodes_dictionary
    
    def init_labyrinth_graph(self):
        """
        Initializes self._labyrinth as a GridCellGraph 
        that contains all the map divide in sectors of CELL_AREA.

        The sectors will be represented as Nodes and the full labyrinth 
        will be a GridCellGraph structure
        """

        # The structure of this list is [ [first_xline_nodes], [second_xline_nodes], [last_xline_node]]
        list_nodes = []
        for y in self.LABYRINTH_COODRS:
            sub_list_x = []
            for x in self.LABYRINTH_COODRS:

                # coords of the 4 edge points of the cell
                left_bottom = Point(x,y)
                right_bottom = Point(x + self.CELL_AREA, y)
                left_upp = Point(x, y + self.CELL_AREA)
                right_upp = Point(x + self.CELL_AREA, y + self.CELL_AREA)
                # area of the cell
                cell_area = Rectangle(left_bottom, left_upp, right_bottom, right_upp)

                cell_node = CellNode(cell_area)

                sub_list_x.append(cell_node)

            list_nodes.append(sub_list_x)
        
        #Once

        

