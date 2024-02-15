from labyrinth.Labyrinth import Labyrinth
from labyrinth.labyrinth_objects import Wall, Door
from labyrinth.two_dimension import Point

MAX_AREA = 200
LONG_DOOR = 1
ERROR_NUM = "-1"
TESEO = Point(0,0)

def create_wall(point_x: int, point_y: int, parallel: bool, longitude: int) -> Wall:
    """
    Create a wall from a start point, the line longitude and if its parallel to (x or y) axes
    """
    first_point = Point(point_x, point_y)
    if parallel :
        #parallel to (y) axis
        second_point = Point(point_x, point_y + longitude)
    else:
        #parallel to (x) axis
        second_point = Point(point_x+ longitude, point_y )

    return Wall(first_point, second_point)

def create_door(point_x: int, point_y: int, parallel: bool) -> Door:
    """
    Create a door from a start point, the line longitude is 1 and if its parallel to (x or y) axes
    """
    first_point = Point(point_x, point_y)
    if parallel :
        #parallel to (y) axis
        second_point = Point(point_x, point_y + LONG_DOOR)
    else:
        #parallel to (x) axis
        second_point = Point(point_x + LONG_DOOR, point_y )
        
    return Door(first_point, second_point)
    
def main(filename: str, labyrinth: Labyrinth = Labyrinth(max_area=MAX_AREA)):
    """
    Reads a file with the description of various labyriths and resolve each labyrith 
    and write it in the output files
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = list(map(lambda x: x.strip(), lines))
        n_walls: int
        n_doors: int
        walls: list[Wall]
        doors: list[Door]
        minotaurs: Point
        while True:
            first_line = lines.pop(0)       # Get the line with M and N
            parts = first_line.split(" ")   # Get the two variables
            if len(parts) != 2: raise Exception("Error: Invalid format file.")
            n_walls = int(parts[0])
            n_doors = int(parts[1])
            if (n_walls == -1)  or (n_doors == -1) : return 1
            elif (n_walls < 0)  or (n_doors < 0): raise Exception("Error: Invalid format file.")
            walls = []
            # Get the walls of the labyrinth
            for i in range(n_walls):
                ith_line = lines.pop(0)
                ith_line = ith_line.split(" ")
                if len(ith_line) != 4: raise Exception("Error: Invalid format file.")
                x_init = int(ith_line[0])
                y_init = int(ith_line[1])
                d_parallel = bool(int(ith_line[2]))
                t_long = int(ith_line[3])
                wall = create_wall(x_init, y_init, d_parallel, t_long)
                walls.append(wall)
            doors = []
            #Get the doors of the labyrinth
            for i in range(n_doors):
                ith_line = lines.pop(0)
                ith_line = ith_line.split(" ")
                if len(ith_line) != 3: raise Exception("Error: Invalid format file.")
                x_init = int(ith_line[0])
                y_init = int(ith_line[1])
                d_parallel = bool(int(ith_line[2]))
                door = create_door(x_init, y_init, d_parallel)
                doors.append(door)
            
            #Get the minotaurs position
            minotaurs_line = lines.pop(0)
            minotaurs_line = minotaurs_line.split(" ")
            if len(minotaurs_line) != 2: raise Exception("Error: Invalid format file.")
            m_x = float(minotaurs_line[0])
            m_y = float(minotaurs_line[1])
            minotaurs = Point(m_x, m_y)
            #Initialize the Labyrinth
            labyrinth.eliminate_labyrinth_objs()
            labyrinth.minotaurs = minotaurs
            labyrinth.add_labyrinth_objs(walls=walls, doors=doors)
            
            labyrinth.print_path_teseo_to_minotaurs()
            #labyrinth.print_solution() not because how big are
                
                    
if __name__ == '__main__':
    labyrinth: Labyrinth = Labyrinth(teseo=TESEO, max_area=MAX_AREA)
    main("../data_files/input.txt", labyrinth)
                
