from .labyrinth_objects import Door, Wall
from .two_dimension import Point, Rectangle
from .graphs import CellNode, GridCellGraph


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
        _labyrinth_nodes: list[list[CellNode]]
            List with list of nodes in the labyrinth in row order
    """
    MIN_COORD = 0
    MAX_COORD = 300
    LABYRINTH_COORDS = range(MIN_COORD, MAX_COORD) # coordenates for x and y

    CELL_AREA = 1 # 1 (unit^2), area of sectors, the min area of a cell in the labyrinth map

    def __init__(self, minotaurs: Point = Point(0,0), walls: 'list[Wall]' = [], doors: 'list[Door]' = []):
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
        

        #Create the structure of the labyrinth without the labyrinth objects
        self._labyrinth_nodes = self._create_nodes()                         # Create the nodes
        self._graph_dictionary = self._associate_nodes(self._labyrinth_nodes) # Dictionary contains the graph nodes
        self.add_labyrinth_objs(self._walls, self._doors)            
    

    def _create_nodes(self) ->'list[list[CellNode]]':
        """
        Creates the nodes of the graph.

        The map of the labyrinth is divided in squares of 1(u^2) and each square is a node,
        The max and the min coordinates are in the costant self.LABYRINTH_COORDS

        return:
            A list with the structure:
                [ [first_xline_nodes], [second_xline_nodes], [last_xline_node]]
        """
        # The structure of this list is [ [first_xline_nodes], [second_xline_nodes], [last_xline_node]]
        list_nodes = []
        for y in self.LABYRINTH_COORDS :
            sub_list_x = []
            for x in self.LABYRINTH_COORDS :

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
        return list_nodes
    
    def _associate_nodes(self, nodes_list: 'list[list[CellNode]]') -> dict:
        """
        Associate the nodes with the node that should be its neighbours.
        Creates the GridCellNode structure of the labyrinth.

        return:
            Return a Dictionary {CellNode:GridCellGraph}

        A node is neightbour to its continous nodes, north one, south one, east one, west one.
        Warning, edge nodes are a especial case
        """

        graph_dictionary = {}
        for j in self.LABYRINTH_COORDS:
            for i in self.LABYRINTH_COORDS:
                
                #Case for corners of the map
                if (i == 0) and (j == 0):
                    north_node = nodes_list[i+1][j]
                    south_node = None
                    west_node = None
                    east_node = nodes_list[i][j+1]

                elif (i == 0) and (j == self.MAX_COORD-1):
                    north_node = nodes_list[i+1][j]
                    south_node = None
                    west_node = nodes_list[i][j-1]
                    east_node = None

                elif (i == self.MAX_COORD-1) and (j == 0):
                    north_node = None
                    south_node = nodes_list[i-1][j]
                    west_node = None
                    east_node = nodes_list[i][j+1]

                elif (i == self.MAX_COORD-1) and ( j == self.MAX_COORD-1):
                    north_node = None
                    south_node = nodes_list[i-1][j]
                    west_node = nodes_list[i][j-1]
                    east_node = None

                #Case for edge lines
                elif i == 0:
                    north_node = nodes_list[i+1][j]
                    south_node = None
                    west_node = nodes_list[i][j-1]
                    east_node = nodes_list[i][j+1]

                elif i == self.MAX_COORD-1:
                    north_node = None
                    south_node = nodes_list[i-1][j]
                    west_node = nodes_list[i][j-1]
                    east_node = nodes_list[i][j+1]

                elif j == 0:
                    north_node = nodes_list[i+1][j]
                    south_node = nodes_list[i-1][i]
                    west_node = None
                    east_node = nodes_list[i][j+1]

                elif j == self.MAX_COORD-1:
                    north_node = nodes_list[i+1][j]
                    south_node = nodes_list[i-1][j]
                    west_node = nodes_list[i][j-1]
                    east_node = None

                #Normal case fo nodes with all neighbours
                else:
                    north_node = nodes_list[i+1][j]
                    south_node = nodes_list[i-1][j]
                    west_node = nodes_list[i][j-1]
                    east_node = nodes_list[i][j+1]
                
                actual_node = nodes_list[i][j]

                # create the grid graph relations
                grid_cell_node = GridCellGraph(actual_node=actual_node, 
                                               north_node=north_node, 
                                               south_node=south_node, 
                                               west_node=west_node, 
                                               east_node=east_node)
                
                graph_dictionary[actual_node] = grid_cell_node

        return graph_dictionary


    def add_labyrinth_objs(self, walls: 'list[Wall]', doors: 'list[Door]'):
        pass

    def eliminate_labyrinth_obs(self, labyrinth_graph: GridCellGraph):
        pass

    def init_labyrinth_graph(self):
        """
        Initializes self._labyrinth as a GridCellGraph 
        that contains all the map divide in sectors of CELL_AREA.

        The sectors will be represented as Nodes and the full labyrinth 
        will be a GridCellGraph structure
        """
    
    

    def _reconstruct_path(came_from: dict, current_node: CellNode) -> 'list[CellNode]':
        """
        Return list with the path to reach the current node from a start node.
        
        Using backtracking of dictionary structure {current_node : came_from_node}.

        Arguments:
            came_from: dict{CellNode : Cell:Node}
                Dictionary with all the nodes used and the parent node
            current_node: CellNode
                Node to get the path from the start
        return: 
            list[CellNode], that are in inverse order of the path =
            [current, parent, grandparent, ..., grandgrand..., start]
        """

        total_path = [current_node]
        while came_from.get(current_node):
            current_node = came_from[current_node]
            total_path.append(current_node)
        
        return total_path
