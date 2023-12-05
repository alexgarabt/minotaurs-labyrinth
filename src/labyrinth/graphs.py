from .two_dimension import Point, Rectangle
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
    def __init__(self, area: Rectangle, north_obj=None, south_obj=None, west_obj=None, east_obj=None):
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
        return hash(self.cell)
    
    def __eq__(self, other: 'CellNode') -> bool:
        if not(isinstance(other, CellNode)): return False
        return self.cell == other.cell
    
    def __repr__(self) -> str:
        return "".join([self.cell.__repr__(), 
                       ", north_obj=", self.north_obj.__repr__(), 
                       ", south_obj=", self.south_obj.__repr__(),
                       ", east_obj=", self.east_obj.__repr__(),
                       ", west_obj=", self.west_obj.__repr__()])

    
class GridCellGraph:

    def __init__(self, actual_node: CellNode, north_node: CellNode= None, south_node: CellNode =None, west_node: CellNode = None,  east_node: CellNode= None):
        self.actual_node = actual_node
        self.north_node = north_node
        self.south_node = south_node
        self.west_node = east_node
        self.east_node = west_node

    def __hash__(self) -> int:
        return hash(self.actual_node)
    
    def __repr__(self) -> str:
        return "".join(["ACTUAL: ",
                        self.actual_node.__repr__(),
                        ", NEIGHBOURS: ",
                        self.north_node.__repr__(), "; ",
                        self.south_node.__repr__(), "; ",
                        self.east_node.__repr__(), "; ",
                        self.west_node.__repr__(), "; "
                        ])


