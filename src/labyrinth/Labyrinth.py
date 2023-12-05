from .labyrinth_objects import Door, Wall
from .two_dimension import Point, Rectangle
from .graphs import CellNode, GridCellGraph
import math


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
        

        # Create the structure of the labyrinth without the labyrinth objects
        # Structure [ [first_xline_nodes], [second_xline_nodes], [last_xline_node]]
        self._labyrinth_nodes = self._create_nodes()                         # Create the nodes, list with all the nodes
        
        # Structure {CellNode:GridCellGrap} the nodes are keys to its graph structure
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

            The actual node is the key, and the GridCellGraph of that node is the value.

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

    def get_node_contains(self, point: Point) -> CellNode:
        """
        Gets the node that contains this point.
        
        Requires that the self._labyrinth_nodes is initialized

        If a point its in the edges of various nodes, 
        it returns the most UPPER & LEFT node that contains the point.

        return:
            One CellNode that contains the point.
            If no node contains the point in the self._labyrinth_nodes, it returns None.
        """

        x = math.floor(point.x)
        y = math.floor(point.y)

        if((len(self._labyrinth_nodes) >= y) and (len(self._labyrinth_nodes[0]) >= x)):
            return self._labyrinth_nodes[y][x]
        return None

    def _add_labyrinth_walls_lenght_1(self, walls: 'list[Wall]'):
        """
        Add the Wall in the list to the cells that contains it

        Wall lenght should be 1.
        
        Labyrinth nodes must be created before and also associated
        So requires the self._graph_dictionary initialized
        
        Arguments:
            walls: list[Wall]
                list with walls to add into the labyrinth
        """
        for ith in walls:
                
                #Get the medium point to get a edge point in onle one edge of the rectangle in the node
                medium_x = (ith.edge1.x + ith.edge2.x)/2
                medium_y = (ith.edge2.y + ith.edge2.y)/2
                medium_p = Point(medium_x, medium_y)

                #Get one of the node that contains the door
                actual_node: CellNode = self.get_node_contains(medium_p)
                if(actual_node == None): continue

                #Get the graph of the node, for get the associated nodes
                grid_graph_node: GridCellGraph = self._graph_dictionary[actual_node]

                # Get the other nodes that contains the door
                if(ith.is_parallel_to_X()):

                    # The door is in the bottom line of the actual node,
                    # So the south node of the actual node have also the door in its north line
                    if(actual_node.cell.bottom_line.contains_point(medium_p)):
                        actual_node.south_obj = ith
                        grid_graph_node.south_node.north_obj = ith

                    # The door is in the upper line of the actual node,
                    # So the north node of the actual node have also the door in its south line
                    elif(actual_node.cell.upper_line.contains_point(medium_p)):
                        actual_node.north_obj = ith
                        grid_graph_node.north_node.south_obj = ith

                elif(ith.is_parallel_to_Y()):

                    # The door is in the left line of the actual node,
                    # So the west node of the actual node have also the door in its east line
                    if(actual_node.cell.left_line.contains_point(medium_p)):
                        actual_node.west_obj = ith
                        grid_graph_node.west_node.east_obj = ith

                    # The door is in the upper line of the actual node,
                    # So the east node of the actual node have also the door in its west line
                    elif(actual_node.cell.right_line.contains_point(medium_p)):
                        actual_node.east_obj = ith
                        grid_graph_node.east_node.west_obj = ith
    
    def _add_labyrinth_walls(self, walls: 'list[Wall]'):
        
        # We will divid the walls into walls of length 1 and add it to the labyrinth
        list_new_walls = []
        for ith_wall in walls:
            #ith_wall: Wall
            list_new_walls.extend(ith_wall.divide_wall_into_1_length())
        
        self._add_labyrinth_walls_lenght_1(list_new_walls)

    def _add_labyrinth_doors(self, doors: 'list[Door]'):
        self._add_labyrinth_walls_lenght_1(doors)

    def add_labyrinth_objs(self, walls: 'list[Wall]'=[], doors: 'list[Door]'=[]):
        """
        Add the doors and the walls into the labyrinth

        See more in the stringdoc of the used methods
        """

        # First the walls, because doors should overwrite walls if they have the same cell
        # Second the doors, to overwrite the walls in the same cell
        self._add_labyrinth_walls(walls)
        self._add_labyrinth_doors(doors)

    def eliminate_labyrinth_objs(self):
        #iterate throuth the keys that are the nodes
        for node in self._graph_dictionary:
            #node: CellNode
            node.north_obj = None
            node.south_obj = None
            node.west_obj = None
            node.east_obj = None

    def A_STAR_SEARCH(self):
        pass
    
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
        
        return total_pathl
        
