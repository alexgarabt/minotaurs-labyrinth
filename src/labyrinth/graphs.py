from labyrinth_objects import Wall
from labyrinth_objects import Door
from two_dimension import Rectangle
from two_dimension import Point
from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    OEAST = 4

class CellNode:
    """
    CellNode represents a rectangle cell with four sides

    Each side can contain a object who tells the Node how to interact in the edges 
    and how to pass to other cell or it can contais nothing in that side.

    If a side contains Wall as object it couldnt pass to that cell
    If a side contains a Door as object it could pass
    If a side contains None it could pass

    Atributtes:
        cell: Rectangle
            The area of the cell
        north_obj: Any
            Object who defines how to act to pass to north cell
        south_obj: Any
            Object who defines how to act to pass to south cell
        east_obj: Any
            Object who defines how to act to pass to east cell
        west_obj: Any
            Object who defines how to act to pass to west cell

    """
    def __init__(self, area: Rectangle):
        self.cell = area

    def __init__(self, area: Rectangle, north_obj, south_obj, east_obj, west_obj):
        self.cell = area
        self.north_obj = north_obj
        self.south_obj = south_obj
        self.east_obj = east_obj
        self.west_obj = west_obj
    
    def contains(self, point: Point) -> bool:
        """
        Tells if a point is in the area of the node
        """
        return self.cell.contains(point)
    
    def distance(self, point: Point) -> float:
        """
        Tells the distance of this node cell to the provied point
        """
        return self.cell.distance(point)
    
    def set_cost_goal(self, cost: float):
        
        self.cost_to_goal = cost

    def __hash__(self) -> int:
        return hash(self.area)

    
class GridCellGraph:
    def __init__(self, node: CellNode):
        self.actual_node = node
        self.north_node = None
        self.south_node = None
        self.east_node = None
        self.west_node = None

    def __init__(self, actual_node: CellNode, 
                 north_node: CellNode, 
                 south_node: CellNode, 
                 east_node: CellNode, 
                 west_node: CellNode):
        self.actual_node = actual_node
        self.north_node = north_node
        self.south_node = south_node
        self.east_node = east_node
        self.west_node = west_node
    


