import time
import os


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

# Convert from index to x, y coordinates
def get_xy(i, size_x):
    x = i % size_x
    y = i // size_x

    return [x, y]

# Convert from x, y coordinates to index
def get_i(x, y, size_x):
    return y * size_x + x



start_time = time.perf_counter()    # 1
# maze = AutomataMaze()
# maze.define()
# maze.read_input("input1.txt")
# result = maze.find_path()
# end_time = time.perf_counter()      # 2
# run_time = end_time - start_time    # 3
# print(f"Found a path with {len(result['path'])} steps in {run_time:.4f} secs")
# save_result_directions(result["directions"])
# print("Saved result.txt!")

# Read maze
file_path = "input1.txt"
maze = []
size_x = 0
size_y = 0

cell_value = 0

initial_i = -1
final_i = -1

# Read the input file
with open(file_path, 'r') as file_handler:
    lines = file_handler.readlines()

# Process input lines and create maze data
y = 0
for line in lines:
    x = 0
    for c in line:
        if is_int(c):
            cell_value = int(c)
            if cell_value == 3:
                initial_i = len(maze)
                # cell_value = 0
            elif cell_value == 4:
                final_i = len(maze)
                # cell_value = 0
            maze.append(cell_value)
        x += 1
    y += 1
    if size_x == 0:
        size_x = len(maze)
size_y = len(maze) // size_x

initial_pos = get_xy(initial_i, size_x)
target_pos = get_xy(final_i, size_x)

maze_state = maze
print(f"Finished reading maze data with {size_x} rows and {size_y} columns")
