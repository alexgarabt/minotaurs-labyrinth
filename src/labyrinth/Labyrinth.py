from .labyrinth_objects import Door, Wall
from .two_dimension import Point, Rectangle
from .graphs import Direction, CellNode, GridCellGraph, PriorityQueue
import math


class Labyrinth:
    """
    Minotaurs Labyrinth representation, the labyrinth is made of Walls and Doors, 
    the walls aren't passables and the doors are.

    The labyrinth contains the minotaurs that is defined by his position and 
    we have Teseo that is also defined by his position.

    The dimensions of the labyrinth are inside [MIN_COORD, MAX_COORD] for X and Y plane

    Teseo Position is in the origin of the coordenates in the postion TESEO

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
        _graph_dictionary: dict[CellNode : GridCellGraph]
            Dictionary that contains all the graph structure, 
            each node is associated to its graph structure as pair (key:value)
    """
    MIN_COORD = 0
    MAX_COORD = 10 #min is 6 #300

    LABYRINTH_COORDS = range(MIN_COORD, MAX_COORD) # coordenates for x and y
    CELL_AREA = 1 # 1 (unit^2), area of sectors, the min area of a cell in the labyrinth map
    # Cost of the labyrinth_objects
    DOOR_COST = 1
    WALL_COST = float('inf')
    EMPTY_COST = 0
    TESEO = Point(0,0)

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
        self.teseo = self.TESEO   # Teseo is in the origin Postion
        

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
        for i in self.LABYRINTH_COORDS:
            for j in self.LABYRINTH_COORDS:
                
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
                    south_node = nodes_list[i-1][j]
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

    def get_node_contains(self, point: Point) -> 'list[CellNode]':
        """
        Gets the nodes that contains this point.
        
        Requires that the self._labyrinth_nodes is initialized

        If a point its in the edges of various nodes, it returns all the nodes
        If the point its not in the coordenates, it returns a empty list

        return:
            One CellNode that contains the point.
            If no node contains the point, then return a empty list
        """

        result = []
        floor_x = math.floor(point.x)
        floor_y = math.floor(point.y)

        # Check if the point is in the coordinates
        if(floor_y > len(self._labyrinth_nodes)) or (floor_x > len(self._labyrinth_nodes[0])):
            return result
        
        # Case of edge Point the point is shared by 4 nodes: In the edge Point of each node
        if ((point.x - floor_x) == 0) and ((point.y - floor_y) == 0):
            #get the upper_right node
            upper_right = None
            upper_left = None
            bottom_right = None
            bottom_left = None

            if floor_x == 0 and floor_y == 0:
                upper_right = self._labyrinth_nodes[floor_y][floor_x]

            elif floor_x == self.MAX_COORD and floor_y == self.MAX_COORD:
                bottom_left = self._labyrinth_nodes[floor_y-1][floor_x-1]

            elif floor_x == 0 and floor_y == self.MAX_COORD:
                bottom_right = self._labyrinth_nodes[floor_y-1][floor_x]

            elif floor_x == self.MAX_COORD and floor_y == 0:
                upper_left = self._labyrinth_nodes[floor_y][floor_x-1]

            elif floor_x == 0:
                upper_right = self._labyrinth_nodes[floor_y][floor_x]
                bottom_right = self._labyrinth_nodes[floor_y-1][floor_x]

            elif floor_y == 0:
                upper_left = self._labyrinth_nodes[floor_y][floor_x-1]
                upper_right = self._labyrinth_nodes[floor_y][floor_x]
            
            elif floor_x == self.MAX_COORD:
                upper_left = self._labyrinth_nodes[floor_y][floor_x-1]
                bottom_left = self._labyrinth_nodes[floor_y-1][floor_x-1]

            elif floor_y == self.MAX_COORD:
                bottom_left = self._labyrinth_nodes[floor_y-1][floor_x-1]
                bottom_right = self._labyrinth_nodes[floor_y-1][floor_x]
            else:
                upper_right = self._labyrinth_nodes[floor_y][floor_x]
                upper_left = self._labyrinth_nodes[floor_y][floor_x-1]
                bottom_right = self._labyrinth_nodes[floor_y-1][floor_x]
                bottom_left = self._labyrinth_nodes[floor_y-1][floor_x-1]

            result.extend([upper_left, upper_right, bottom_left, bottom_right])
                
        # Case the point is shared by 2 nodes: In the north of one and in the south of the other.
        elif (point.y - floor_y) == 0:
            

            if floor_y == 0:
                bottom = None
                upper = self._labyrinth_nodes[floor_y][floor_x]

            elif floor_y == self.MAX_COORD:
                bottom = self._labyrinth_nodes[floor_y-1][floor_x]
                upper = None
            else:
                upper = self._labyrinth_nodes[floor_y][floor_x]
                bottom = self._labyrinth_nodes[floor_y-1][floor_x]

            result.extend([bottom, upper])

        # Case the point is shared by 2 nodes: In the west of one and in the east of the other.
        elif (point.x - floor_x) == 0:
            
            if floor_x == 0:
                right = self._labyrinth_nodes[floor_y][floor_x]
                left = None

            if floor_x == self.MAX_COORD:
                left = self._labyrinth_nodes[floor_y][floor_x-1]
                right = None
            else:
                left = self._labyrinth_nodes[floor_y][floor_x-1]
                right = self._labyrinth_nodes[floor_y][floor_x]

            result.extend([right, left])

        # Normal case the point is only inside of a node
        else:
            result.append(self._labyrinth_nodes[floor_x][floor_y])
        
        result = list(filter(lambda x: x is not None, result))
        return result

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
        
        for wall in walls:
                #Get the medium point to get a edge point in onle one edge of the rectangle in the node
                medium_x = (wall.edge1.x + wall.edge2.x)/2
                medium_y = (wall.edge1.y + wall.edge2.y)/2
                medium_p = Point(medium_x, medium_y)

                #Get one of the node that contains the door
                list_node: list[CellNode] = self.get_node_contains(medium_p)
                #not node contains the wall
                if not list_node: 
                    continue

                
                if(wall.is_parallel_to_X()):
                    for node in list_node:
                        if(node.cell.bottom_line.contains_point(medium_p)):
                            node.south_obj = wall
                        elif(node.cell.upper_line.contains_point(medium_p)):
                            node.north_obj = wall

                elif(wall.is_parallel_to_Y()):
                    for node in list_node:
                        if(node.cell.left_line.contains_point(medium_p)):
                            node.west_obj = wall
                        elif(node.cell.right_line.contains_point(medium_p)):
                            node.east_obj = wall
                               
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

    def _cost(self, node: CellNode, direction: Direction) -> float:
        """
        Tells the cost of a node to move in the given direction
        """
        obj = node.get_obj_in_direction(direction)

        if isinstance(obj, Door): return self.DOOR_COST
        elif isinstance(obj, Wall): return self.WALL_COST
        else: return self.EMPTY_COST

    def _heuristic(self, node: CellNode, goal: CellNode) -> float:
        """
        Heuristic uses the manhattan distance between the center of nodes
        """
        return node.manhattan_distance(goal.cell.center)
    
    def A_STAR_SEARCH(self, start: CellNode, goal: CellNode):
        """
        A* algorithm of heuristic search for graphs
        For fiding the minimum path between two nodes
        
        Args:
            start: CellNode
                Start node of the path
            goal: CellNode
                Goal node to reach from the start node

        """
        # f(n) = g(n) + h(n)
        # g(n) = cost of (n) node is the cost from the (start) node to (n) node.
        # h(n) = heuristic cost, is manhattan distance between centers of nodes.

        frontier = PriorityQueue() # Initialize the priority queue
        frontier.put(start, 0)     # Put the start node in the queue
        
        came_from: dict[CellNode, CellNode] = {} # Dictionary to record the track of how every node is reached
        cost_so_far: dict[CellNode, float] = {}  # g(n): Dictionary will store the cost to the key node 
        came_from[start] = None # The start is reached from none
        cost_so_far[start] = 0  # Initialize the cost, g(start) = 0
    
        while not frontier.empty():
            current: CellNode = frontier.get() # Get the node with the best f(n) = g(n) + h(n)
            
            if current is goal:
                return True, came_from, cost_so_far
                #break
            
            # Obtain the graph of the current node
            graph_node: GridCellGraph = self._graph_dictionary[current]


            # Check the neighbours of the current node
            for next in graph_node.get_neighbours(): 
                
                next_node: CellNode = next[0]
                direction: Direction = next[1]

                # Get the cost of this node g(next_node) = g(current) + cost(next_node)
                new_cost = cost_so_far[current] + self._cost(current, direction)
                # If the cost is (inf) => the path is unreachable

                if(new_cost >= float('inf')): 
                    continue

                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:

                    # Set the g(nex_node)
                    cost_so_far[next_node] = new_cost

                    # Set the f(next_node) = g(next_node) + h(next_node)
                    priority = new_cost + self._heuristic(next_node, goal)
                    frontier.put(next_node, priority)
                    came_from[next_node] = current

        #The goal is not reachable
        return False, came_from, cost_so_far

    def _reconstruct_path(self, came_from: dict, current_node: CellNode) -> 'list[CellNode]':
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

    def teseo_to_minotaurs(self):
        """
        Get the min path from teseo to the minotaurs
        
        return:
            list[0]: bool
                If its possible to reach a path
            list[1]: list[CellNode]
                A list with nodes from teseo to minotaurs
            list[2]: int
                number of doors used in the path"""
         
        path = []
        teseo_node: CellNode = self.get_node_contains(self.teseo)[0]
        minotaurs_node: CellNode = self.get_node_contains(self.minotaurs)[0]

        if(teseo_node is None or minotaurs_node is None): 
            raise ValueError("Error: Minotaurs must be in the labyrinth coordenates")
         
        list_search = self.A_STAR_SEARCH(teseo_node, minotaurs_node)
         
        
        is_possible = list_search[0]
        came_from = list_search[1]
        costs = list_search[2]
        number_of_doors_used = costs[minotaurs_node]

        if is_possible:
            
            path = self._reconstruct_path(came_from, minotaurs_node)[::-1]
            

        return is_possible, path, number_of_doors_used
    
    def print_path_teseo_to_minotaurs(self):
        """
        Print basic information from the resolution of reach the minotaurs
        """
        result = self.teseo_to_minotaurs()
        is_possible = result[0]
        number_of_doors_used = result[2]
        path = result[1]

        print("---------------------------------------")
        print("Is possible to resolve?:", is_possible)
        if is_possible:
            print("Number of doors used:", number_of_doors_used)
            print("Number of cells used:", len(path))
            print("---------------------------------------")
            print("\nPath:")
            for i in path:
                print(i)

    def _get_labyrinth_matrix(self, list_nodes:'list[CellNode]' =[]) -> 'list[list[str]]':
        """
        Return a basic matrix with the labyrinth representated
        
        No doors or walls are represented.
        Teseo is represented as T
        Minotaurs is represented as M
        Provided nodes are represented as #
        """
        result = []
        reverse = self._labyrinth_nodes[::-1]
        for i in reverse:
            sub = []
            j: CellNode
            for j in i:
                if j.contains(self.teseo) and j.contains(self.minotaurs):
                    sub.append("|T/M|")
                elif j.contains(self.teseo):
                    sub.append("|T|")
                elif j.contains(self.minotaurs):
                    sub.append("|M|")
                elif j in list_nodes:
                    sub.append("|#|")
                else: 
                    sub.append("| |")
            result.append(sub)
        return result
    
    def _print_labyrith(self, list_nodes:'list[CellNode]' =[]):
        """
        Prints in the standar output the labyrinth
        Usefull for small labyrinths
        """
        martix = self._get_labyrinth_matrix(list_nodes)
        for list in martix:
            for i in list:
                print(i, end="")
            print()

    def print_solution(self):
        """Print in the standard output a graphic basic resolution of the labyrinth"""
        print("\nLabyrinth:")
        self._print_labyrith()
        print("\nSolution:")
        self._print_labyrith(self.teseo_to_minotaurs()[1])   

        

                
         
        
