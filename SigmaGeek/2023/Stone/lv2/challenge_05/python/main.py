# Stone Sigma Geek - Lv02 - Challenge 05
import numpy as np
from numpy.fft import fft2, ifft2

import codecs

import psutil
import time
import sys
import os


# Cell constants
UNKNOWN_CELL = 5
FINAL_CELL   = 4
INITIAL_CELL = 3
LIVE_CELL    = 1 # Green
DEAD_CELL    = 0 # White

# MATRIX_TYPE  = np.byte
MATRIX_TYPE  = np.uint8

# Debug constant
# For debugging, only change it to true
# Then the process is pause in each iteraction
# Allowing the class variables to be inspected
DEBUG_MODE = "--debug" in sys.argv


def fft_convolve2d(board, kernal):
    #  Compute the 2D FFT of the input array board and the kernel kernal.
    board_ft = fft2(board)
    kernal_ft = fft2(kernal)
    height, width = board_ft.shape
    # Computes the inverse FFT of the product of the 2D FFTs of the input array and kernel. 
    # The result is a complex array, so we take only the real part.
    convolution = np.real(ifft2(board_ft * kernal_ft))
    # shift the zero-frequency component to the center of the spectrum.
    convolution = np.roll(convolution, - int(height // 2), axis=0)
    convolution = np.roll(convolution, - int(width // 2), axis=1)
    # returns the convolution result rounded to nearest integer.
    return convolution.round()

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
        start_time = time.perf_counter()    # 1
        with open(file_path, 'r') as f:
            lines = f.readlines()
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Read file content in {run_time:.4f} secs")

        start_time = time.perf_counter()    # 1
        # Process input lines and create maze data
        y = 0
        for line in lines:
            x = 0
            maze_line = []
            for c in line:
                if c in ["0", "1", "2", "3", "4"]:
                    cell_value = int(c)
                    if cell_value == INITIAL_CELL:
                        self.initial_pos = [x, y]
                        cell_value = 0
                    elif cell_value == FINAL_CELL:
                        self.target_pos = [x, y]
                        cell_value = 0
                    maze_line.append(cell_value)
                    x += 1
            maze.append(maze_line)
            y += 1
            if self.size_x == 0:
                self.size_x = len(maze_line)
        self.size_y = len(maze)

        self.maze_state = np.array(maze, dtype=MATRIX_TYPE)
        self.next_maze_state = np.full((self.size_y, self.size_x), 0, dtype=MATRIX_TYPE)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Created matrix in {run_time:.4f} secs")
        print(f"Finished reading maze data with {self.size_y} rows and {self.size_x} columns")

        self.total_alive_cells = np.count_nonzero(self.maze_state)

        shape = self.maze_state.shape
        shape = (shape[0] + 2, shape[1] + 2)

        neighborhood = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        n_height, n_width = neighborhood.shape
        self.kernal = np.zeros(shape)
        self.kernal[(shape[0] - n_height) // 2 : ((shape[0] - n_height) // 2) + n_height,
                    (shape[1] - n_width) // 2 : ((shape[1] - n_width) // 2) + n_width] = neighborhood

    # Find path through the maze
    def find_first_particle_path(self):
        current_t = 0

        self.iteration_which_maze_stabilize = -1

        directions = []
        # Find the best cells to switch states
        # target_states = self.switch_states_of_best_cells(30)
        # for target_state in target_states:
        #     directions.append("A")
        #     directions.append("%d" % (target_state[0],))
        #     directions.append("%d" % (target_state[1],))

        # Initialize position list
        current_pos_list = [
            {
                # Positions follows this format: x, y, t
                "pos": np.array([self.initial_pos[0], self.initial_pos[1]]),
                "path": [],
                "directions": directions
            }
        ]
        # max_pos_list_size = self.size_x + self.size_y + 1
        # max_pos_list_size = max(self.size_x, self.size_y)/2
        max_pos_list_size = 250

        self.max_path_repetition = 4
        max_t = 10000000
        while current_t < max_t:
            current_t += 1
            start_time = time.perf_counter()    # 1

            next_pos_list = []

            # Define possible movements
            possible_movements = { 
                "U": np.array([ 0, -1]),
                "D": np.array([ 0,  1]),
                "L": np.array([-1,  0]),
                "R": np.array([ 1,  0]),
            }
            best_pos_distance = self.size_x * self.size_y * 10000

            print("Movements analized: ", len(current_pos_list), " (t ", current_t, ")")
            if DEBUG_MODE:
                for pd in current_pos_list: 
                    print(pd["pos"])
                import pdb; pdb.set_trace() # Start debugger

            directions_to_add = []

            # Perf improvements
            if self.total_alive_cells > 0:
                self.calculate_next_state()
            else:
                self.target_pos = [139, 290]
                if self.iteration_which_maze_stabilize == -1:
                    self.iteration_which_maze_stabilize = current_t
                max_pos_list_size = 20

            # Analyze movements
            for pos in current_pos_list:
                for mov in possible_movements:
                    next_pos = pos["pos"] + possible_movements[mov]
                    if self.is_valid_pos(next_pos, pos["path"], next_pos_list):
                        next_pos_data = {
                            "pos": next_pos,
                            "path": pos["path"] + [next_pos],
                            "dist": self.sqrdist(next_pos, self.target_pos),
                            "directions": pos["directions"] + [mov] + directions_to_add
                        }
                        if next_pos_data["dist"] < best_pos_distance:
                            best_pos_distance = next_pos_data["dist"]
                        if next_pos[0] == self.target_pos[0] and next_pos[1] == self.target_pos[1]:
                            return next_pos_data
                        next_pos_list.append(next_pos_data)
            if len(next_pos_list) > max_pos_list_size:
                next_pos_list = sorted(next_pos_list, key=lambda x: x["dist"])
                next_pos_list = next_pos_list[:max_pos_list_size]
            current_pos_list = next_pos_list
            print(" - Best dist ", best_pos_distance, "")
            print(" - Memory: ", get_memory_usage())

            self.maze_state = self.next_maze_state

            end_time = time.perf_counter()      # 2
            run_time = end_time - start_time    # 3
            print(f" - Iteration run in {run_time:.4f} secs")

        return False

    def find_path_for_all_particles(self):
        first_particle_path = self.find_first_particle_path()
        first_particle_total_steps = len(first_particle_path["path"])

        print(f"Found a path for first particle with {len(first_particle_path['path'])} steps")

        # Directions from (138, 299)
        next_directions_from_new_initial_points = []
        for x in range(0, 80):
            next_directions_from_new_initial_points += ['R']
            next_directions_from_new_initial_points += ['U'] * 299 
            next_directions_from_new_initial_points += ['R']
            next_directions_from_new_initial_points += ['D'] * 299

        first_particle_direction = first_particle_path['directions'] + next_directions_from_new_initial_points

        # Directions for particles
        particle_directions = (["D"] * 299) + (["R"] * 138)
        particle_directions += next_directions_from_new_initial_points

        particle_str = " ".join(particle_directions)

        total_remain_particles = 48140
        t = 359
        with codecs.open("output5.txt", 'w', 'utf-8') as file_handler:
            file_handler.write("0 " + " ".join(first_particle_direction) + "\n")
            for p in range(0, total_remain_particles):
                file_handler.write(f"{t} {particle_str}\n")
                t += 1
        print("Saved output5.txt!")

    def calculate_next_state(self):
        self.rule = [[4,5], [2,3,4]]
        start_time = time.perf_counter()    # 1
        padding_maze_state = np.pad(self.maze_state, ((1, 1), (1, 1)), 'constant', constant_values=0)
        convolution = fft_convolve2d(padding_maze_state, self.kernal)
        self.convolution = convolution
        shape = convolution.shape
        new_board = np.zeros(shape, dtype=MATRIX_TYPE)

        new_board[np.where(np.in1d(convolution, self.rule[0]).reshape(shape)
                           & (padding_maze_state == LIVE_CELL))] = LIVE_CELL
        new_board[np.where(np.in1d(convolution, self.rule[1]).reshape(shape)
                           & (padding_maze_state == DEAD_CELL))] = LIVE_CELL

        # Remove padding
        new_board = new_board[1:-1, 1:-1]

        new_board[self.initial_pos[1], self.initial_pos[0]] = DEAD_CELL
        new_board[self.target_pos[1], self.target_pos[0]] = DEAD_CELL

        self.next_maze_state = new_board
        self.total_alive_cells = np.count_nonzero(self.next_maze_state)
        print(" - Total alive cells: ", self.total_alive_cells)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f" - Calculated next maze state in {run_time:.4f} secs")

    # Check if the position is valid (inside the maze and not a dead cell)
    def is_valid_pos(self, pos, path, next_pos_list):
        return pos[0] >= 0 and pos[0] < self.size_x and \
               pos[1] >= 0 and pos[1] < self.size_y and \
               self.next_maze_state[pos[1], pos[0]] == DEAD_CELL and \
               not [p for p in next_pos_list if p["pos"][0] == pos[0] and p["pos"][1] == pos[1]] and \
               len([p for p in path[-10:] if p[0] == pos[0] and p[1] == pos[1]]) <= self.max_path_repetition


    # Calculate the squared distance between two vectors
    def sqrdist(self, v1, v2):
        return (v1[0] - v2[0]) * (v1[0] - v2[0]) + (v1[1] - v2[1]) * (v1[1] - v2[1])

    # Print the maze state at a specific time
    def print_maze(self):
        print_state(self.maze_state, self.size_x, self.size_y)

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

def print_array(nparray):
    rows, cols = nparray.shape

    for i in range(rows):
        row = ''
        for j in range(cols):
            row += str(int(nparray[i,j]))
        print(row)

def print_state(state, state_size_x, state_size_y):
    rows = state_size_y
    cols = state_size_x

    for i in range(rows):
        row = ''
        for j in range(cols):
            row += str(state[i,j])
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
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "input5.txt"
    start_time = time.perf_counter()    # 1
    maze = AutomataMaze()
    maze.read_input(file_path)
    maze.find_path_for_all_particles()
    end_time = time.perf_counter()      # 2
    run_time = end_time - start_time    # 3
    print(f"Found a result in {run_time:.4f} secs")
    # print(f"Maze stabilized in step {maze.iteration_which_maze_stabilize}")
