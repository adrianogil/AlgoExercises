import numpy as np

import psutil
import time
import os


# Cell constants
UNKNOWN_CELL = 5
FINAL_CELL   = 4
INITIAL_CELL = 3
LIVE_CELL    = 1 # Green
DEAD_CELL    = 0 # White

# Debug constant
# For debugging, only change it to true
# Then the process is pause in each iteraction
# Allowing the class variables to be inspected
DEBUG_MODE = False

# Main class for solving the maze
class AutomataMaze:
    def __init__(self):
        self.maze_states = []
        self.size_x = 0
        self.size_y = 0
        self.initial_pos = []
        self.target_pos = []

    # Read input from file and initialize maze
    def read_input(self, file_path):
        maze = []

        initial_i = -1
        final_i = -1

        # Read the input file
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # Process input lines and create maze data
        y = 0
        for line in lines:
            x = 0
            for c in line:
                if is_int(c):
                    cell_value = int(c)
                    if cell_value == INITIAL_CELL:
                        initial_i = len(maze)
                        # cell_value = 0
                    elif cell_value == FINAL_CELL:
                        final_i = len(maze)
                        # cell_value = 0
                    maze.append(cell_value)
                x += 1
            y += 1
            if self.size_x == 0:
                self.size_x = len(maze)
        self.size_y = len(maze) // self.size_x

        self.initial_pos = self.get_xy(initial_i)
        self.target_pos = self.get_xy(final_i)

        # self.maze_state = np.array(maze, dtype=np.byte)
        # self.next_maze_state = np.array(maze, dtype=np.byte)

        self.maze_states.append(np.array(maze, dtype=np.uint8))
        print(f"Finished reading maze data with {self.size_y} rows and {self.size_x} columns")

    # Find path through the maze
    def find_path(self):
        current_t = 0

        # Initialize position list
        current_pos_list = [
            {
                # Positions follows this format: x, y, t
                "pos": [self.initial_pos[0], self.initial_pos[1], current_t],
                "path": [],
                "directions": []
            }
        ]
        max_pos_list_size = self.size_x * self.size_y + 1

        max_path_repetition = 4
        max_t = 10000000
        while current_t < max_t:
            current_t += 1

            next_pos_list = []

            # Define possible movements
            possible_movements = { 
                "U": [ 0, -1, 1],
                "D": [ 0,  1, 1],
                "L": [-1,  0, 1],
                "R": [ 1,  0, 1],
            }
            best_pos_distance = self.size_x * self.size_y * 10000

            # Perf improvements
            self.calculate_all_state(current_t)
            self.maze_states[current_t - 1] = []

            print("Movements analized: ", len(current_pos_list), " (t ", current_t, ")")
            if DEBUG_MODE:
                for pd in current_pos_list: 
                    print(pd["pos"])
                import pdb; pdb.set_trace() # Start debugger

            # Analyze movements
            for pos in current_pos_list:
                for mov in possible_movements:
                    next_pos = self.vecsum(pos["pos"], possible_movements[mov])
                    if self.is_valid_pos(next_pos):
                        next_pos_data = {
                            "pos": next_pos,
                            "path": pos["path"] + [next_pos],
                            "dist": self.sqrdist(next_pos, self.target_pos),
                            "directions": pos["directions"] + [mov]
                        }
                        if next_pos_data["dist"] < best_pos_distance:
                            best_pos_distance = next_pos_data["dist"]
                        if next_pos[0] == self.target_pos[0] and next_pos[1] == self.target_pos[1]:
                            return next_pos_data

                        # Check if position already exists
                        if not [p for p in next_pos_list if p["pos"][0] == next_pos[0] and p["pos"][1] == next_pos[1]]:
                            # Check if position is too much repeated in the past
                            path_repetion = len([p for p in next_pos_data["path"][-10:] \
                                if p[0] == next_pos[0] and p[1] == next_pos[1]])
                            if path_repetion <= max_path_repetition:
                                next_pos_list.append(next_pos_data)
            if len(next_pos_list) > max_pos_list_size:
                next_pos_list = sorted(next_pos_list, key=lambda x: x["dist"])
                next_pos_list = next_pos_list[:max_pos_list_size]
            current_pos_list = next_pos_list
            print(" - Best dist ", best_pos_distance, "")
            print(" - Memory: ", get_memory_usage())

        return False

    # Get cell value in the maze for given coordinates and time
    def get_cell_value(self, x, y, t):
        current_maze_t = len(self.maze_states)
        if t >= current_maze_t:
            # add new maze states
            for new_t in range(current_maze_t, t + 1):
                self.maze_states.append(np.full((self.size_y * self.size_x, 1), UNKNOWN_CELL))
                self.maze_states[new_t][self.get_i(*self.initial_pos)] = INITIAL_CELL
                self.maze_states[new_t][self.get_i(*self.target_pos)] = FINAL_CELL
    
        return self.calculate_cell_value(x, y, t)

    def calculate_all_state(self, t):
        for x in range(0, self.size_x):
            for y in range(0, self.size_y):
                self.get_cell_value(x, y, t)

    # Calculate cell value for given coordinates and time
    def calculate_cell_value(self, x, y, t):
        i = self.get_i(x, y)

        if t <= 0:
            return self.maze_states[0][i]
        if self.maze_states[t][i] != UNKNOWN_CELL:
            return self.maze_states[t][i]

        last_cell_value = self.get_cell_value(x, y, t - 1)

        # Calculate live and dead neighbor cells
        live_neighbors = 0
        dead_neighbors = 0

        cell_value = DEAD_CELL
        for k in range(0, 9):
            xk = (k % 3) - 1
            yk = (k // 3) - 1

            xn = x + xk
            yn = y + yk

            if (xk != 0 or yk != 0) and xn >= 0 and xn < self.size_x and yn >= 0 and yn < self.size_y:
                neightbor_value = self.get_cell_value(xn, yn, t - 1)
                if neightbor_value == LIVE_CELL:
                    live_neighbors += 1

        # Propagation rule
        # 
        # - White cells (DEAD_CELL) turn green (LIVE_CELL) if they have a number of green adjacent cells greater than 1 and less
        # than 5. Otherwise, they remain white (DEAD_CELL).
        # - Green cells (LIVE_CELL) remain green if they have a number of green adjacent cells greater than 3 and
        # less than 6. Otherwise, they become white (DEAD_CELL).

        if last_cell_value == DEAD_CELL and live_neighbors in [2,3,4]:
            cell_value = LIVE_CELL
        elif last_cell_value == LIVE_CELL and live_neighbors in [4,5]:
            cell_value = LIVE_CELL

        self.maze_states[t][i] = cell_value
        return cell_value

    # Check if the position is valid (inside the maze and not a dead cell)
    def is_valid_pos(self, pos):
        return pos[0] >= 0 and pos[0] < self.size_x and \
               pos[1] >= 0 and pos[1] < self.size_y and \
               pos[2] >= 0 and \
               self.get_cell_value(*pos) in [DEAD_CELL, INITIAL_CELL, FINAL_CELL]

    # Calculate the sum of two vectors
    def vecsum(self, v1, v2):
        vs = []
        for i in range(0, len(v1)):
            vs.append(v1[i] + v2[i])
        return vs

    # Calculate the squared distance between two vectors
    def sqrdist(self, v1, v2):
        return (v1[0] - v2[0]) * (v1[0] - v2[0]) + (v1[1] - v2[1]) * (v1[1] - v2[1])

    # Print the maze state at a specific time
    def print_maze(self, t):
        print_state(self.maze_states[t], self.size_x, self.size_y)

    # Convert from index to x, y coordinates
    def get_xy(self, i):
        x = i % self.size_x
        y = i // self.size_x

        return [x, y]

    # Convert from x, y coordinates to index
    def get_i(self, x, y):
        return y * self.size_x + x


#### Utils ####
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def print_state(state, state_size_x, state_size_y):
    rows = state_size_y
    cols = state_size_x

    for i in range(rows):
        row = ''
        for j in range(cols):
            index = i * cols + j
            row += str(state[index]) + ' '
        row += ' - ' + str(i)
        print(row)

def save_result_directions(result_directions):
    directions_string = " ".join(result_directions)

    with open("result.txt", 'w') as file_handler:
        file_handler.write(directions_string)


def sizeof_fmt(num, suffix='B'):
    """
        Returns human readable byte
        https://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
    """
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def get_memory_usage(human_format=True):
    process = psutil.Process(os.getpid())
    memory_value_bytes = process.memory_info().rss
    if human_format:
        memory_value_human_read = sizeof_fmt(memory_value_bytes)
        memory_usage = memory_value_human_read
    else:
        memory_usage = memory_value_bytes

    return memory_usage


if __name__ == '__main__':
    start_time = time.perf_counter()    # 1
    maze = AutomataMaze()
    maze.read_input("input1.txt")
    result = maze.find_path()
    end_time = time.perf_counter()      # 2
    run_time = end_time - start_time    # 3
    print(f"Found a path with {len(result['path'])} steps in {run_time:.4f} secs")
    save_result_directions(result["directions"])
    print("Saved result.txt!")
