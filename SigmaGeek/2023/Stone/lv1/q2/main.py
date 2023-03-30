
UNKNOWN_CELL = 5
FINAL_CELL   = 4
INITIAL_CELL = 3
LIVE_CELL    = 1
DEAD_CELL    = 0


class AutomataMaze:
    def __init__(self):
        self.maze_states = []
        self.size_x = 0
        self.size_y = 0
        self.initial_pos = []
        self.target_pos = []

    def read_input(self, file_path):
        maze = []

        initial_i = -1
        final_i = -1


        with open(file_path, 'r') as f:
            lines = f.readlines()

        for line in lines:
            for c in line:
                if is_int(c):
                    cell_value = int(c)
                    if cell_value == INITIAL_CELL:
                        initial_i = len(maze)
                    elif cell_value == FINAL_CELL:
                        final_i = len(maze)
                    maze.append(cell_value)
            if self.size_x == 0:
                self.size_x = len(maze)
        self.size_y = len(maze) // self.size_x

        self.maze_states.append(maze)
        print(f"Finished reading maze data with {self.size_y} rows and {self.size_x} columns")

    def find_path(self):
        return {
            "path": []
        }


#### Utils ####
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    maze = AutomataMaze()
    maze.read_input("input.txt")
    result = maze.find_path()
    print(f"Found a path with {len(result['path'])} steps")
