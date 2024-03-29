## These file include the object that could be in the labyrinth
from .two_dimension import Point, FiniteLine

class Wall(FiniteLine):
    """
    Simple wall representation in two dimensional plane

    The wall is parallel to X or Y axes,
    The wall width is infinitesimally small 
    and the height is infinitesimally large.
    The length of the Wall is variable but its a positive integer

    Wall edge1 is at the left/bottom and Wall edge2 is at the right/upp

    So the wall cant be jumped or traspased.
    """
    def __init__(self, left_or_botton: Point, right_or_top: Point):
        """
        Initialices the line of the wall and check if its parallel to an axis
        """
        super().__init__(left_or_botton, right_or_top)

        if  not(self.is_parallel_to_X) and not(self.is_parallel_to_Y):
            raise ValueError("Error: Line is not parallel to X or Y axes")
        
        if (self.length < 0): 
            raise ValueError("Error: wall shoul be constructued (left -> right) or (bottom -> top)")
        try:
            int(self.length)
        except ValueError: 
            raise ValueError("Error: wall length should be a integer")
    
    def divide_wall_into_1_length(self) -> 'list[Wall]':
        """
        Divide the actual wall into walls of 1 length
        
        return:
            A list with all the new walls
        """
        LENGTH = 1

        result = []
        for j in range(0, int(self.length)):

                first_edge_x = self.edge1.x
                first_edge_y = self.edge1.y

                second_edge_x = first_edge_x
                second_edge_y = first_edge_y

                if(self.is_parallel_to_X()):
                    first_edge_x += LENGTH*(j)
                    second_edge_x += 1 + LENGTH*(j)
                
                elif(self.is_parallel_to_Y()):
                    first_edge_y += LENGTH*(j)
                    second_edge_y += 1 + LENGTH*(j)

                f_point = Point(first_edge_x, first_edge_y)
                s_point = Point(second_edge_x, second_edge_y)
                result.append(Wall(f_point, s_point))
        
        return result
    
    def is_a_door(self):
        return False
    
    def __repr__(self) -> str:
        return super().__repr__() + "[W]"
    
    def get_str(self) -> str:
        return "walls.append(Wall(Point"+self.edge1.__repr__()+", Point"+self.edge2.__repr__()+"))"

class Door(Wall):
    """
    Simple Door implementation.

    The door is a passable wall but the 
    length of the door is always 1.
    """

    DOOR_LENGTH = 1

    def __init__(self, left_or_botton: Point, right_or_top: Point):

        super().__init__(left_or_botton, right_or_top)
        if self.length != self.DOOR_LENGTH:
            raise ValueError("Error: distance between points should be 1")
    
    def is_a_door(self):
        return False
    
    def __repr__(self) -> str:
        return super().__repr__() + "[D]"
    
    def get_str(self) -> str:
        return "doors.append(Door(Point"+self.edge1.__repr__()+", Point"+self.edge2.__repr__()+"))"




        
        
        