import json


import numpy as np


def get_next_state(state, size_x, size_y):
    next_state = [1]

    for i in range(1, len(state) - 1):
        xs = i % size_x
        ys = i // size_x

        current_pattern = []

        live_neighbors = 0
        dead_neighbors = 0
        next_value = 1
        for k in range(0, 9):
            xk = (k % 3) - 1
            yk = (k // 3) - 1

            xn = xs + xk
            yn = ys + yk

            if (xk != 0 or yk != 0) and xn >= 0 and xn < size_x and yn >= 0 and yn < size_y:
                it = yn * size_x + xn
                live_neighbors += state[it]
                if not state[it]:
                    dead_neighbors += 1
        print(dead_neighbors)
        if state[i] and dead_neighbors in [2,3]:
            next_value = 0
        elif not state[i] and live_neighbors <= 4:
            next_value = 0
        next_state.append(next_value)
    next_state += [1]
    return next_state


def next_state_conway(state, size_x, size_y):
    next_state = [1]

    for i in range(1, len(state) - 1):
        xs = i % size_x
        ys = i // size_x

        current_pattern = []

        live_neighbors = 0
        next_value = 1
        for k in range(0, 9):
            xk = (k % 3) - 1
            yk = (k // 3) - 1

            xn = xs + xk
            yn = ys + yk

            if xk != 0 and yk !=0 and xn >= 0 and xn < size_x and yn >= 0 and yn < size_y:
                it = yn * size_x + xn
                live_neighbors += state[it]
        if state[i] and live_neighbors < 2:
            next_value = 0
        elif not state[i] and live_neighbors < 3:
            next_value = 0
        next_state.append(next_value)
    next_state += [1]
    return next_state


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



def find_path_in_maze(states_data, size_x, size_y):

    states = []

    for state_data in states_data:
        states += [state_data["state"]]

    print("First state:")
    print_state(states[0], size_x, size_y)
    print()

    # Try to find patterns in current states
    dead_patterns = {}

    for s in range(1, len(states)):
        for i in range(1, len(states[s]) - 1):
            if states[s][i] == 0: # Dead cell
                xs = i % size_x
                ys = i // size_x

                current_pattern = []

                for k in range(0, 9):
                    xk = (k % 3) - 1
                    yk = (k // 3) - 1

                    xn = xs + xk
                    yn = ys + yk

                    if xn >= 0 and xn < size_x and yn >= 0 and yn < size_y:
                        it = yn * size_x + xn
                        current_pattern.append[states[s][i][it]]
                    else:
                        current_pattern.append[1]



if __name__ == '__main__':
    with open('mazestates.json', 'r') as f:
        maze_data = json.load(f)
    # find_path_in_maze(maze_data["states"], maze_data["mazeSizeX"], maze_data["mazeSizeY"])
    next_state = get_next_state(maze_data["states"][1]["state"], maze_data["mazeSizeX"], maze_data["mazeSizeY"])

    print_state(maze_data["states"][1]["state"], maze_data["mazeSizeX"], maze_data["mazeSizeY"])
    print("Next:")
    print_state(next_state, maze_data["mazeSizeX"], maze_data["mazeSizeY"])
